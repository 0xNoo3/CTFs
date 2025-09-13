#include <bits/stdc++.h>
#include <cstdint>
using namespace std;
using u64 = uint64_t;
using u8  = uint8_t;

// --- Parameters from the Rust challenge ---
static constexpr int    WINDOW   = 5;
static constexpr u64    PRIME    = 2147483647;
static constexpr u64    BASE     = 256;
static constexpr u64    SEED     = 2;          // (days_since_epoch % 7) on 2025-05-17
static constexpr u64    PERM_KEY = 0x42424242;
static constexpr u32    XOR_SEED = 0x13371337;

// Expected rolling-hashes at offsets 0,5,10,15,20:
static const map<int,u64> EXPECTED = {
    {0,  1910641389},
    {5,   978734675},
    {10,  639015185},
    {15,  434697744},
    {20,  977939275},
};

// Fast modular multiply
inline u64 modmul(u64 a, u64 b){
    return (unsigned __int128)a * b % PRIME;
}

// Undo the +((i*SEED)%256) time‐mutation
vector<u8> invert_time(const vector<u8>& m) {
    vector<u8> t(m.size());
    for(int i = 0; i < (int)m.size(); i++)
        t[i] = m[i] - static_cast<u8>((i * SEED) % 256);
    return t;
}

// Undo transform_input’s two‐pass XOR
vector<u8> invert_transform(const vector<u8>& t) {
    int n = t.size();
    vector<u8> b(t.begin(), t.end());
    // Reverse pass2
    for(int i = n-1; i > 0; i--)
        b[i] ^= (b[i-1] >> 3);
    // Reverse pass1
    for(int i = 0; i < n; i++){
        u8 mask = (XOR_SEED >> (i % 32)) & 0xFF;
        b[i] ^= mask;
    }
    return b;
}

// Undo permute():
string invert_permute(const vector<u8>& b) {
    int n = b.size();
    vector<pair<int,int>> swaps;
    swaps.reserve(n);
    for(int i = 0; i < n; i++){
        int j = (u64(i) * PERM_KEY) % n;
        swaps.emplace_back(i, j);
    }
    vector<u8> a = b;
    for(int k = n-1; k >= 0; k--){
        auto [i,j] = swaps[k];
        swap(a[i], a[j]);
    }
    return string((char*)a.data(), a.size());
}

// Solve one 5-byte window at position pos by MITM
void solve_window(int pos, vector<u8>& mutated) {
    u64 H = EXPECTED.at(pos);

    // Precompute two-byte partial hashes: h0 = b0*256^4 + b1*256^3
    unordered_map<u64, uint16_t> head;
    head.reserve(1<<16);
    u64 p4 = 1;
    for(int i = 0; i < 4; i++) p4 = modmul(p4, BASE);
    u64 p3 = modmul(p4, (BASE + PRIME - 1) / BASE);

    for(int b0 = 0; b0 < 256; b0++){
      for(int b1 = 0; b1 < 256; b1++){
        u64 h0 = (u64(b0) * p4 + u64(b1) * p3) % PRIME;
        head[h0] = (b0 << 8) | b1;
      }
    }

    // Try all triples (b2,b3,b4) and lookup the head
    for(int b2 = 0; b2 < 256; b2++){
      for(int b3 = 0; b3 < 256; b3++){
        for(int b4 = 0; b4 < 256; b4++){
          u64 tail = ((u64(b2)<<16) + (u64(b3)<<8) + b4) % PRIME;
          u64 need = (H + PRIME - tail) % PRIME;
          auto it = head.find(need);
          if(it != head.end()){
            uint16_t v = it->second;
            mutated[pos+0] = v >> 8;
            mutated[pos+1] = v & 0xFF;
            mutated[pos+2] = b2;
            mutated[pos+3] = b3;
            mutated[pos+4] = b4;
            return;
          }
        }
      }
    }

    cerr << "[!] failed at window " << pos << endl;
    exit(1);
}

int main(){
    // We only need 25 bytes (0..24)
    vector<u8> mutated(25);
    for(auto [pos,_] : EXPECTED)
        solve_window(pos, mutated);

    // Invert the remaining transforms
    auto tbytes = invert_time(mutated);
    auto xbytes = invert_transform(tbytes);
    string flag = invert_permute(xbytes);

    cout << "Recovered flag: " << flag << "\n";
    return 0;
}
