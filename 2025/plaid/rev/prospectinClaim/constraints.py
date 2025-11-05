from z3 import *

# input = {offset: BitVec(f"input[{offset}]", 8) for offset in range(0, 64)}
input = [BitVec(f"input[{index}]", 8) for index in range(0, 64)]


Constraints = []

Constraints.append( input[27] == 50 )
 
Constraints.append( (input[31] ^ input[24]) == 0xAA )
 
Constraints.append( (input[31] + input[46]) == 144 )
 
Constraints.append( (input[59] + input[36]) == 129 )
 
Constraints.append( input[13] == 190 )
 
Constraints.append( input[32] == 100 )
 
Constraints.append( input[26] == 49 )
 
Constraints.append( input[42] == 57 )
 
Constraints.append( (input[45] + input[63]) == 147 )
 
Constraints.append( input[50] == 49 )
 
Constraints.append( (input[1] + input[15]) == 56 )
 
Constraints.append( (input[13] ^ input[35]) == 0x8E )
 
Constraints.append( (input[1] ^ input[46]) == 0x71 )
 
Constraints.append( input[42] == 180 )
 
Constraints.append( input[19] == 54 )
 
Constraints.append( input[28] == input[48] )
 
Constraints.append( (input[10] ^ input[33]) == 3 )
 
Constraints.append( input[30] == 118 )
 
Constraints.append( input[5] == 50 )
 
Constraints.append( (input[1] ^ input[48]) == 0x85 )
 
Constraints.append( input[2] == 84 )
 
Constraints.append( input[23] == 225 )
 
Constraints.append( (input[9] ^ input[54]) == 0x81 )
 
Constraints.append( (input[53] + input[26]) == 97 )
 
Constraints.append( (input[18] ^ input[57]) == 7 )
 
Constraints.append( (input[18] ^ input[5]) == 0x56 )
 
Constraints.append( (input[14] + input[53]) == 102 )
 
Constraints.append( (input[48] ^ input[56]) == 0x54 )
 
Constraints.append( input[52] == 229 )
 
Constraints.append( input[36] == 111 )
 
Constraints.append( (input[37] + input[30]) == 102 )
 
Constraints.append( input[50] == 49 )
 
Constraints.append( input[23] == 56 )
 
Constraints.append( input[39] == 52 )
 
Constraints.append( (input[56] + input[19]) == 151 )
 
Constraints.append( (input[19] ^ input[50]) == 0x2D )
 
Constraints.append( (input[34] + input[1]) == 164 )
 
Constraints.append( (input[47] + input[38]) == 244 )
 
Constraints.append( (input[27] + input[47]) == 151 )
 
Constraints.append( (input[47] + input[10]) == 150 )
 
Constraints.append( input[2] == 114 )
 
Constraints.append( input[59] == 54 )
 
Constraints.append( input[28] == 177 )
 
Constraints.append( (input[8] ^ input[58]) == 8 )
 
Constraints.append( (input[2] ^ input[46]) == 0x3A )
 
Constraints.append( input[59] == 68 )
 
Constraints.append( input[57] == 18 )
 
Constraints.append( (input[17] ^ input[40]) == 0x5B )
 
Constraints.append( input[41] == 42 )
 
Constraints.append( input[41] == 51 )
 
Constraints.append( (input[26] + input[38]) == 63 )
 
Constraints.append( (input[61] ^ input[0]) == 0x60 )
 
Constraints.append( input[21] == 36 )
 
Constraints.append( (input[5] + input[43]) == 45 )
 
Constraints.append( input[57] == 99 )
 
Constraints.append( (input[55] ^ input[52]) == 5 )
 
Constraints.append( input[4] == 123 )
 
Constraints.append( (input[16] + input[9]) == 173 )
 
Constraints.append( (input[22] + input[45]) == 152 )
 
Constraints.append( input[24] == 50 )
 
Constraints.append( input[48] == 53 )
 
Constraints.append( (input[54] ^ input[19]) == 0x5B )
 
Constraints.append( (input[54] + input[14]) == 153 )
 
Constraints.append( input[53] == 210 )
 
Constraints.append( (input[0] ^ input[48]) == 0x65 )
 
Constraints.append( (input[42] + input[49]) == 154 )
 
Constraints.append( (input[20] + input[29]) == 150 )
 
Constraints.append( (input[40] ^ input[50]) == 0xDA )
 
Constraints.append( (input[60] + input[32]) == 150 )
 
Constraints.append( (input[39] + input[7]) == 152 )
 
Constraints.append( input[50] == input[10] )
 
Constraints.append( (input[57] ^ input[10]) == 0x52 )
 
Constraints.append( input[56] == 97 )
 
Constraints.append( input[20] == 97 )
 
Constraints.append( (input[62] ^ input[8]) == 1 )
 
Constraints.append( (input[44] ^ input[34]) == 0x30 )
 
Constraints.append( input[33] == 50 )
 
Constraints.append( (input[47] ^ input[49]) == 4 )
 
Constraints.append( (input[27] ^ input[22]) == 0x53 )
 
Constraints.append( (input[0] + input[41]) == 131 )
 
Constraints.append( input[18] == 241 )
 
Constraints.append( input[28] == 53 )
 
Constraints.append( input[16] == 211 )
 
Constraints.append( (input[6] + input[47]) == 153 )
 
Constraints.append( (input[28] + input[25]) == 175 )
 
Constraints.append( (input[63] + input[19]) == 179 )
 
Constraints.append( input[29] == 53 )
 
Constraints.append( input[61] == 48 )
 
Constraints.append( (input[15] + input[25]) == 133 )
 
Constraints.append( (input[20] ^ input[61]) == 0x4F )
 
Constraints.append( (input[27] ^ input[50]) == 3 )
 
Constraints.append( (input[62] + input[51]) == 98 )
 
Constraints.append( (input[20] + input[44]) == 197 )
 
Constraints.append( (input[43] + input[18]) == 201 )
 
Constraints.append( (input[9] + input[36]) == 104 )
 
Constraints.append( input[9] == input[19] )
 
Constraints.append( (input[19] ^ input[33]) == 4 )
 
Constraints.append( (input[55] + input[0]) == 133 )
 
Constraints.append( input[22] == 97 )
 
Constraints.append( input[17] == 57 )
 
Constraints.append( input[10] == 49 )
 
Constraints.append( input[53] == 48 )
 
Constraints.append( (input[49] + input[61]) == 233 )
 
Constraints.append( input[50] == 49 )
 
Constraints.append( (input[55] + input[3]) == 191 )
 
Constraints.append( (input[45] + input[25]) == 153 )
 
Constraints.append( input[46] == 50 )
 
Constraints.append( (input[24] + input[43]) == 151 )
 
Constraints.append( input[26] == 49 )
 
Constraints.append( input[14] == 54 )
 
Constraints.append( (input[3] + input[62]) == 118 )
 
Constraints.append( input[27] == 50 )
 
Constraints.append( (input[63] ^ input[45]) == 0x4A )
 
Constraints.append( (input[44] + input[14]) == 240 )
 
Constraints.append( input[9] == 216 )
 
Constraints.append( (input[58] + input[62]) == 98 )
 
Constraints.append( (input[61] + input[22]) == 147 )
 
Constraints.append( (input[51] ^ input[53]) == 2 )
 
Constraints.append( input[27] == 50 )
 
Constraints.append( (input[50] ^ input[59]) == 7 )
 
Constraints.append( input[52] == 48 )
 
Constraints.append( input[33] == 121 )
 
Constraints.append( input[61] == 51 )
 
Constraints.append( (input[21] + input[49]) == 197 )
 
Constraints.append( input[36] == 83 )
 
Constraints.append( input[15] == 9 )
 
Constraints.append( (input[0] + input[32]) == 180 )
 
Constraints.append( (input[14] + input[51]) == 104 )
 
Constraints.append( (input[43] ^ input[14]) == 0xFB )
 
Constraints.append( input[58] == 79 )
 
Constraints.append( input[10] == 62 )
 
Constraints.append( input[47] == 236 )
 
Constraints.append( input[45] == 55 )
 
Constraints.append( (input[22] + input[59]) == 255 )
 
Constraints.append( (input[24] ^ input[2]) == 0x28 )
 
Constraints.append( input[48] == 209 )
 
Constraints.append( (input[55] ^ input[7]) == 0xE8 )
 
Constraints.append( input[47] == 101 )
 
Constraints.append( (input[5] + input[57]) == 252 )
 
Constraints.append( (input[24] + input[5]) == 100 )
 
Constraints.append( (input[34] ^ input[54]) == 2 )
 
Constraints.append( input[9] == 54 )
 
Constraints.append( input[5] == 50 )
 
Constraints.append( input[26] == 49 )
 
Constraints.append( input[60] == 50 )
 
Constraints.append( (input[4] + input[7]) == 223 )
 
Constraints.append( input[31] == 52 )
 
Constraints.append( (input[50] ^ input[52]) == 0x59 )
 
Constraints.append( input[58] == 57 )
 
Constraints.append( (input[12] ^ input[43]) == 0x53 )
 
Constraints.append( input[7] == 97 )
 
Constraints.append( (input[53] ^ input[7]) == 0x54 )
 
Constraints.append( (input[59] + input[6]) == 106 )
 
Constraints.append( (input[17] + input[28]) == 110 )
 
Constraints.append( input[4] == 123 )
 
Constraints.append( input[35] == 101 )
 
Constraints.append( (input[36] + input[44]) == 150 )
 
Constraints.append( input[63] == 125 )
 
Constraints.append( (input[27] ^ input[41]) == 0x5D )
 
Constraints.append( input[40] == 98 )
 
Constraints.append( (input[24] ^ input[21]) == 0x63 )
 
Constraints.append( (input[21] ^ input[19]) == 0x52 )
 
Constraints.append( input[10] == 49 )
 
Constraints.append( (input[37] + input[6]) == 103 )
 
Constraints.append( input[6] == 123 )
 
Constraints.append( input[56] == 147 )
 
Constraints.append( (input[9] ^ input[29]) == 3 )
 
Constraints.append( input[47] == 199 )
 
Constraints.append( input[29] == 53 )
 
Constraints.append( input[63] == 125 )
 
Constraints.append( (input[51] + input[38]) == 71 )
 
Constraints.append( (input[60] + input[20]) == 147 )
 
Constraints.append( (input[1] ^ input[15]) == 0x74 )
 
Constraints.append( (input[11] ^ input[58]) == 0x16 )
 
Constraints.append( input[50] == 49 )
 
Constraints.append( (input[0] + input[63]) == 205 )
 
Constraints.append( input[60] == 50 )
 
Constraints.append( input[54] == 99 )
 
Constraints.append( input[7] == 75 )
 
Constraints.append( (input[29] ^ input[40]) == 0x57 )
 
Constraints.append( input[58] == 57 )
 
Constraints.append( (input[33] ^ input[44]) == 0x56 )
 
Constraints.append( input[17] == 150 )
 
Constraints.append( input[19] == 171 )
 
Constraints.append( (input[59] + input[51]) == 175 )
 
Constraints.append( input[21] == 127 )
 
Constraints.append( (input[35] ^ input[11]) == 0xD1 )
 
Constraints.append( input[40] == 98 )
 
Constraints.append( (input[18] ^ input[13]) == 0x5E )
 
Constraints.append( input[7] == 22 )
 
Constraints.append( (input[54] + input[6]) == 151 )
 
Constraints.append( input[50] == 49 )
 
Constraints.append( input[45] == 55 )
 
Constraints.append( (input[19] + input[5]) == 104 )
 
Constraints.append( input[4] == 26 )
 
Constraints.append( input[62] == 48 )
 
Constraints.append( (input[12] ^ input[24]) == 4 )
 
Constraints.append( (input[46] + input[32]) == 150 )
 
Constraints.append( input[34] == 97 )
 
Constraints.append( input[3] == 70 )
 
Constraints.append( (input[11] + input[47]) == 151 )
 
Constraints.append( input[46] == 50 )
 
Constraints.append( input[25] == 96 )
 
Constraints.append( input[9] == 54 )
 
Constraints.append( input[26] == 58 )
 
Constraints.append( (input[55] ^ input[42]) == 0xC )
 
Constraints.append( (input[34] ^ input[19]) == 0x57 )
 
Constraints.append( input[56] == 97 )
 
Constraints.append( (input[43] ^ input[31]) == 0x51 )
 
Constraints.append( input[55] == 53 )
 
Constraints.append( input[9] == 169 )
 
Constraints.append( (input[46] + input[3]) == 120 )
 
Constraints.append( input[48] == 31 )
 
Constraints.append( (input[35] + input[23]) == 157 )
 
Constraints.append( input[36] == 109 )
 
Constraints.append( (input[30] ^ input[28]) == 6 )
 
Constraints.append( input[53] == 48 )
 
Constraints.append( input[20] == 247 )
 
Constraints.append( input[50] == 49 )
 
Constraints.append( (input[60] + input[45]) == 105 )
 
Constraints.append( (input[41] ^ input[12]) == 5 )
 
Constraints.append( (input[9] ^ input[42]) == 0x85 )
 
Constraints.append( input[32] == 100 )
 
Constraints.append( input[53] == 48 )
 
Constraints.append( (input[38] + input[55]) == 103 )
 
Constraints.append( input[32] == input[13] )
 
Constraints.append( input[36] == 50 )
 
Constraints.append( input[23] == 155 )
 
Constraints.append( input[13] == 100 )
 
Constraints.append( input[8] == 49 )
 
Constraints.append( input[36] == 50 )
 
Constraints.append( input[14] == 195 )
 
Constraints.append( (input[41] + input[21]) == 151 )
 
Constraints.append( (input[45] + input[37]) == 106 )
 
Constraints.append( input[32] == 50 )
 
Constraints.append( input[44] == 100 )
 
Constraints.append( input[2] == 84 )
 
Constraints.append( (input[35] ^ input[50]) == 0x54 )
 
Constraints.append( input[51] == 50 )
 
Constraints.append( input[48] == 53 )
 
Constraints.append( input[41] == 51 )
 
Constraints.append( input[27] == 50 )
 
Constraints.append( (input[49] + input[59]) == 151 )
 
Constraints.append( input[36] == 50 )
 
Constraints.append( input[22] == 97 )
 
Constraints.append( (input[55] + input[4]) == 18 )
 
Constraints.append( input[46] == 158 )
 
Constraints.append( (input[22] ^ input[31]) == 0x55 )
 
Constraints.append( input[50] == 67 )
 
Constraints.append( input[23] == 56 )
 
Constraints.append( input[52] == 12 )
 
Constraints.append( input[52] == 48 )
 
Constraints.append( input[22] == 97 )
 
Constraints.append( input[14] == 54 )
 
Constraints.append( input[2] == 84 )
 
Constraints.append( (input[8] ^ input[22]) == 0x50 )
 
Constraints.append( (input[35] + input[0]) == 167 )
 
Constraints.append( (input[39] + input[2]) == 199 )
 
Constraints.append( (input[41] ^ input[6]) == 7 )
 
Constraints.append( (input[33] + input[11]) == 165 )
 
Constraints.append( input[25] == 98 )
 
Constraints.append( input[26] == 49 )
 
Constraints.append( (input[20] + input[27]) == 35 )
 
Constraints.append( (input[6] ^ input[35]) == 0x9C )
 
Constraints.append( (input[14] ^ input[11]) == 4 )
 
Constraints.append( input[39] == 52 )
 
Constraints.append( (input[40] + input[31]) == 150 )
 
Constraints.append( input[57] == 99 )
 
Constraints.append( input[7] == 100 )
 
Constraints.append( input[14] == 54 )
 
Constraints.append( input[5] == 67 )
 
Constraints.append( (input[23] ^ input[22]) == 0x59 )
 
Constraints.append( input[21] == 100 )
 
Constraints.append( (input[22] ^ input[44]) == 5 )
 
Constraints.append( input[53] == 48 )
 
Constraints.append( input[31] == 52 )
 
Constraints.append( input[22] == 97 )
 
Constraints.append( (input[46] + input[8]) == 122 )
 
Constraints.append( (input[25] ^ input[3]) == 0x24 )
 
Constraints.append( input[43] == 101 )
 
Constraints.append( input[44] == 15 )
 
Constraints.append( (input[16] ^ input[21]) == 0x57 )
 
Constraints.append( (input[9] ^ input[62]) == 6 )
 
Constraints.append( input[27] == 50 )
 
Constraints.append( (input[18] + input[54]) == 209 )
 
Constraints.append( input[32] == 100 )
 
Constraints.append( (input[57] + input[18]) == 199 )
 
Constraints.append( (input[43] ^ input[32]) == 1 )
 
Constraints.append( input[17] == 164 )
 
Constraints.append( (input[8] ^ input[9]) == 7 )
 
Constraints.append( input[40] == 98 )
 
Constraints.append( (input[56] + input[4]) == 10 )
 
Constraints.append( (input[21] + input[28]) == 153 )
 
Constraints.append( input[12] == 124 )
 
Constraints.append( (input[63] + input[18]) == 225 )
 
Constraints.append( input[27] == 50 )
 
Constraints.append( input[23] == 56 )
 
Constraints.append( (input[44] + input[18]) == 200 )
 
Constraints.append( (input[9] + input[19]) == 108 )
 
Constraints.append( (input[61] + input[11]) == 231 )
 
Constraints.append( input[21] == 100 )
 
Constraints.append( (input[57] + input[31]) == 151 )
 
Constraints.append( (input[28] ^ input[40]) == 0x57 )
 
Constraints.append( input[45] == 55 )
 
Constraints.append( (input[13] + input[47]) == 201 )
 
Constraints.append( input[18] == 100 )
 
Constraints.append( input[15] == 55 )
 
Constraints.append( (input[58] ^ input[16]) == 0xA )
 
Constraints.append( (input[0] ^ input[21]) == 0x34 )
 
Constraints.append( (input[62] + input[49]) == 145 )
 
Constraints.append( input[46] == 50 )
 
Constraints.append( (input[57] + input[0]) == 168 )
 
Constraints.append( input[36] == 50 )
 
Constraints.append( input[50] == 49 )
 
Constraints.append( input[48] == 53 )
 
Constraints.append( input[42] == 57 )
 
Constraints.append( (input[61] + input[35]) == 149 )
 
Constraints.append( (input[27] + input[1]) == 117 )
 
Constraints.append( input[48] == 53 )
 
Constraints.append( (input[35] ^ input[33]) == 0x51 )
 
Constraints.append( (input[29] ^ input[57]) == 0x56 )
 
Constraints.append( input[23] == 75 )
 
Constraints.append( (input[31] + input[13]) == 172 )
 
Constraints.append( input[39] == 74 )
 
Constraints.append( input[39] == 52 )
 
Constraints.append( input[33] == 115 )
 
Constraints.append( input[7] == 100 )
 
Constraints.append( input[0] == 80 )
 
Constraints.append( input[22] == 97 )
 
Constraints.append( (input[62] + input[55]) == 101 )
 
Constraints.append( input[52] == 48 )
 
Constraints.append( (input[7] + input[22]) == 204 )
 
Constraints.append( (input[26] ^ input[14]) == 7 )
 
Constraints.append( input[2] == 84 )
 
Constraints.append( input[46] == 50 )
 
Constraints.append( input[52] == 48 )
 
Constraints.append( (input[54] ^ input[35]) == 6 )
 
Constraints.append( (input[31] ^ input[34]) == 0x55 )
 
Constraints.append( input[33] == 50 )
 
Constraints.append( (input[40] + input[33]) == 148 )
 
Constraints.append( input[7] == 100 )
 
Constraints.append( input[15] == 55 )
 
Constraints.append( (input[10] ^ input[43]) == 0x54 )
 
Constraints.append( input[15] == 55 )
 
Constraints.append( (input[29] + input[30]) == 104 )
 
Constraints.append( (input[43] ^ input[13]) == 1 )
 
Constraints.append( (input[58] + input[24]) == 217 )
 
Constraints.append( (input[17] + input[61]) == 105 )
 
Constraints.append( input[41] == 166 )
 
Constraints.append( (input[54] ^ input[24]) == 0x51 )
 
Constraints.append( input[62] == 48 )
 
Constraints.append( (input[57] + input[37]) == 150 )
 
Constraints.append( (input[61] ^ input[4]) == 0x4B )
 
Constraints.append( (input[37] + input[52]) == 99 )
 
Constraints.append( (input[21] ^ input[26]) == 0x3D )
 
Constraints.append( input[50] == 233 )
 
Constraints.append( (input[5] ^ input[29]) == 7 )
 
Constraints.append( input[31] == 52 )
 
Constraints.append( input[53] == 1 )
 
Constraints.append( (input[15] + input[7]) == 155 )
 
Constraints.append( input[41] == 51 )
 
Constraints.append( (input[35] + input[27]) == 151 )
 
Constraints.append( input[42] == 57 )
 
Constraints.append( input[27] == 50 )
 
Constraints.append( input[47] == 101 )
 
Constraints.append( (input[45] ^ input[30]) == 4 )
 
Constraints.append( input[30] == 51 )
 
Constraints.append( input[22] == 97 )
 
Constraints.append( input[49] == 97 )
 
Constraints.append( (input[31] + input[21]) == 152 )
 
Constraints.append( input[24] == 50 )
 
Constraints.append( input[15] == 55 )
 
Constraints.append( input[35] == 203 )
 
Constraints.append( (input[4] + input[37]) == 174 )
 
Constraints.append( input[49] == 97 )
 
Constraints.append( (input[7] ^ input[31]) == 0x50 )
 
Constraints.append( (input[15] + input[19]) == 109 )
 
Constraints.append( (input[30] ^ input[22]) == 0xC7 )
 
Constraints.append( (input[16] ^ input[60]) == 1 )
 
Constraints.append( input[12] == 54 )
 
Constraints.append( input[28] == 1 )
 
Constraints.append( (input[44] + input[58]) == 157 )
 
Constraints.append( (input[49] ^ input[37]) == 0x52 )
 
Constraints.append( input[6] == 52 )
 
Constraints.append( input[38] == 50 )
 
Constraints.append( input[62] == 48 )
 
Constraints.append( (input[37] ^ input[21]) == 0x57 )
 
Constraints.append( (input[40] + input[5]) == 148 )
 
Constraints.append( (input[11] + input[34]) == 147 )
 
Constraints.append( input[43] == 153 )
 
Constraints.append( (input[22] + input[27]) == 136 )
 
Constraints.append( input[46] == input[38] )
 
Constraints.append( (input[48] ^ input[61]) == 5 )
 
Constraints.append( input[12] == 86 )
 
Constraints.append( (input[44] ^ input[28]) == 0x51 )
 
Constraints.append( input[45] == 55 )
 
Constraints.append( (input[37] ^ input[2]) == 0x67 )
 
Constraints.append( (input[54] ^ input[16]) == 0x7B )
 
Constraints.append( (input[45] ^ input[18]) == 0x91 )
 
Constraints.append( input[18] == 100 )
 