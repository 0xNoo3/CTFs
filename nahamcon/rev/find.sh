#!/usr/bin/env bash
# save this as find_flag.sh, then: chmod +x find_flag.sh

BIN="./flagsflags"
CANDIDATES="candidates.txt"

# get total number of flags
total=$(wc -l < "$CANDIDATES")
echo "[*] Loaded $total candidates."

count=0
while IFS= read -r flag; do
  count=$((count + 1))
  # show progress
  printf "\rTesting [%d/%d]: %s" "$count" "$total" "$flag"

  # send the flag on stdin and capture output
  output=$(printf '%s\n' "$flag" | "$BIN" 2>&1)

  # if output is NOT "Incorrect flag!", we've found it
  if ! grep -q "Incorrect flag!" <<< "$output"; then
    echo -e "\n✅ Found candidate: $flag"
    echo "--- Program output:"
    echo "$output"
    exit 0
  fi
done < "$CANDIDATES"

echo -e "\n❌ Tried all $total flags, none produced a new response."
exit 1
