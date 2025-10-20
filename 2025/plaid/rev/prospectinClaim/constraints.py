from z3 import *

bitvecs = {offset: BitVec(f"input[{offset}]", 8) for offset in range(0, 64)}

conds = []

conds.append( bitvecs[27] == 50 )
 
conds.append( (bitvecs[31] ^ bitvecs[24]) == 0xAA )
 
conds.append( (bitvecs[31] + bitvecs[46]) == 144 )
 
conds.append( (bitvecs[59] + bitvecs[36]) == 129 )
 
conds.append( bitvecs[13] == 190 )
 
conds.append( bitvecs[32] == 100 )
 
conds.append( bitvecs[26] == 49 )
 
conds.append( bitvecs[42] == 57 )
 
conds.append( (bitvecs[45] + bitvecs[63]) == 147 )
 
conds.append( bitvecs[50] == 49 )
 
conds.append( (bitvecs[1] + bitvecs[15]) == 56 )
 
conds.append( (bitvecs[13] ^ bitvecs[35]) == 0x8E )
 
conds.append( (bitvecs[1] ^ bitvecs[46]) == 0x71 )
 
conds.append( bitvecs[42] == 180 )
 
conds.append( bitvecs[19] == 54 )
 
conds.append( bitvecs[28] == bitvecs[48] )
 
conds.append( (bitvecs[10] ^ bitvecs[33]) == 3 )
 
conds.append( bitvecs[30] == 118 )
 
conds.append( bitvecs[5] == 50 )
 
conds.append( (bitvecs[1] ^ bitvecs[48]) == 0x85 )
 
conds.append( bitvecs[2] == 84 )
 
conds.append( bitvecs[23] == 225 )
 
conds.append( (bitvecs[9] ^ bitvecs[54]) == 0x81 )
 
conds.append( (bitvecs[53] + bitvecs[26]) == 97 )
 
conds.append( (bitvecs[18] ^ bitvecs[57]) == 7 )
 
conds.append( (bitvecs[18] ^ bitvecs[5]) == 0x56 )
 
conds.append( (bitvecs[14] + bitvecs[53]) == 102 )
 
conds.append( (bitvecs[48] ^ bitvecs[56]) == 0x54 )
 
conds.append( bitvecs[52] == 229 )
 
conds.append( bitvecs[36] == 111 )
 
conds.append( (bitvecs[37] + bitvecs[30]) == 102 )
 
conds.append( bitvecs[50] == 49 )
 
conds.append( bitvecs[23] == 56 )
 
conds.append( bitvecs[39] == 52 )
 
conds.append( (bitvecs[56] + bitvecs[19]) == 151 )
 
conds.append( (bitvecs[19] ^ bitvecs[50]) == 0x2D )
 
conds.append( (bitvecs[34] + bitvecs[1]) == 164 )
 
conds.append( (bitvecs[47] + bitvecs[38]) == 244 )
 
conds.append( (bitvecs[27] + bitvecs[47]) == 151 )
 
conds.append( (bitvecs[47] + bitvecs[10]) == 150 )
 
conds.append( bitvecs[2] == 114 )
 
conds.append( bitvecs[59] == 54 )
 
conds.append( bitvecs[28] == 177 )
 
conds.append( (bitvecs[8] ^ bitvecs[58]) == 8 )
 
conds.append( (bitvecs[2] ^ bitvecs[46]) == 0x3A )
 
conds.append( bitvecs[59] == 68 )
 
conds.append( bitvecs[57] == 18 )
 
conds.append( (bitvecs[17] ^ bitvecs[40]) == 0x5B )
 
conds.append( bitvecs[41] == 42 )
 
conds.append( bitvecs[41] == 51 )
 
conds.append( (bitvecs[26] + bitvecs[38]) == 63 )
 
conds.append( (bitvecs[61] ^ bitvecs[0]) == 0x60 )
 
conds.append( bitvecs[21] == 36 )
 
conds.append( (bitvecs[5] + bitvecs[43]) == 45 )
 
conds.append( bitvecs[57] == 99 )
 
conds.append( (bitvecs[55] ^ bitvecs[52]) == 5 )
 
conds.append( bitvecs[4] == 123 )
 
conds.append( (bitvecs[16] + bitvecs[9]) == 173 )
 
conds.append( (bitvecs[22] + bitvecs[45]) == 152 )
 
conds.append( bitvecs[24] == 50 )
 
conds.append( bitvecs[48] == 53 )
 
conds.append( (bitvecs[54] ^ bitvecs[19]) == 0x5B )
 
conds.append( (bitvecs[54] + bitvecs[14]) == 153 )
 
conds.append( bitvecs[53] == 210 )
 
conds.append( (bitvecs[0] ^ bitvecs[48]) == 0x65 )
 
conds.append( (bitvecs[42] + bitvecs[49]) == 154 )
 
conds.append( (bitvecs[20] + bitvecs[29]) == 150 )
 
conds.append( (bitvecs[40] ^ bitvecs[50]) == 0xDA )
 
conds.append( (bitvecs[60] + bitvecs[32]) == 150 )
 
conds.append( (bitvecs[39] + bitvecs[7]) == 152 )
 
conds.append( bitvecs[50] == bitvecs[10] )
 
conds.append( (bitvecs[57] ^ bitvecs[10]) == 0x52 )
 
conds.append( bitvecs[56] == 97 )
 
conds.append( bitvecs[20] == 97 )
 
conds.append( (bitvecs[62] ^ bitvecs[8]) == 1 )
 
conds.append( (bitvecs[44] ^ bitvecs[34]) == 0x30 )
 
conds.append( bitvecs[33] == 50 )
 
conds.append( (bitvecs[47] ^ bitvecs[49]) == 4 )
 
conds.append( (bitvecs[27] ^ bitvecs[22]) == 0x53 )
 
conds.append( (bitvecs[0] + bitvecs[41]) == 131 )
 
conds.append( bitvecs[18] == 241 )
 
conds.append( bitvecs[28] == 53 )
 
conds.append( bitvecs[16] == 211 )
 
conds.append( (bitvecs[6] + bitvecs[47]) == 153 )
 
conds.append( (bitvecs[28] + bitvecs[25]) == 175 )
 
conds.append( (bitvecs[63] + bitvecs[19]) == 179 )
 
conds.append( bitvecs[29] == 53 )
 
conds.append( bitvecs[61] == 48 )
 
conds.append( (bitvecs[15] + bitvecs[25]) == 133 )
 
conds.append( (bitvecs[20] ^ bitvecs[61]) == 0x4F )
 
conds.append( (bitvecs[27] ^ bitvecs[50]) == 3 )
 
conds.append( (bitvecs[62] + bitvecs[51]) == 98 )
 
conds.append( (bitvecs[20] + bitvecs[44]) == 197 )
 
conds.append( (bitvecs[43] + bitvecs[18]) == 201 )
 
conds.append( (bitvecs[9] + bitvecs[36]) == 104 )
 
conds.append( bitvecs[9] == bitvecs[19] )
 
conds.append( (bitvecs[19] ^ bitvecs[33]) == 4 )
 
conds.append( (bitvecs[55] + bitvecs[0]) == 133 )
 
conds.append( bitvecs[22] == 97 )
 
conds.append( bitvecs[17] == 57 )
 
conds.append( bitvecs[10] == 49 )
 
conds.append( bitvecs[53] == 48 )
 
conds.append( (bitvecs[49] + bitvecs[61]) == 233 )
 
conds.append( bitvecs[50] == 49 )
 
conds.append( (bitvecs[55] + bitvecs[3]) == 191 )
 
conds.append( (bitvecs[45] + bitvecs[25]) == 153 )
 
conds.append( bitvecs[46] == 50 )
 
conds.append( (bitvecs[24] + bitvecs[43]) == 151 )
 
conds.append( bitvecs[26] == 49 )
 
conds.append( bitvecs[14] == 54 )
 
conds.append( (bitvecs[3] + bitvecs[62]) == 118 )
 
conds.append( bitvecs[27] == 50 )
 
conds.append( (bitvecs[63] ^ bitvecs[45]) == 0x4A )
 
conds.append( (bitvecs[44] + bitvecs[14]) == 240 )
 
conds.append( bitvecs[9] == 216 )
 
conds.append( (bitvecs[58] + bitvecs[62]) == 98 )
 
conds.append( (bitvecs[61] + bitvecs[22]) == 147 )
 
conds.append( (bitvecs[51] ^ bitvecs[53]) == 2 )
 
conds.append( bitvecs[27] == 50 )
 
conds.append( (bitvecs[50] ^ bitvecs[59]) == 7 )
 
conds.append( bitvecs[52] == 48 )
 
conds.append( bitvecs[33] == 121 )
 
conds.append( bitvecs[61] == 51 )
 
conds.append( (bitvecs[21] + bitvecs[49]) == 197 )
 
conds.append( bitvecs[36] == 83 )
 
conds.append( bitvecs[15] == 9 )
 
conds.append( (bitvecs[0] + bitvecs[32]) == 180 )
 
conds.append( (bitvecs[14] + bitvecs[51]) == 104 )
 
conds.append( (bitvecs[43] ^ bitvecs[14]) == 0xFB )
 
conds.append( bitvecs[58] == 79 )
 
conds.append( bitvecs[10] == 62 )
 
conds.append( bitvecs[47] == 236 )
 
conds.append( bitvecs[45] == 55 )
 
conds.append( (bitvecs[22] + bitvecs[59]) == 255 )
 
conds.append( (bitvecs[24] ^ bitvecs[2]) == 0x28 )
 
conds.append( bitvecs[48] == 209 )
 
conds.append( (bitvecs[55] ^ bitvecs[7]) == 0xE8 )
 
conds.append( bitvecs[47] == 101 )
 
conds.append( (bitvecs[5] + bitvecs[57]) == 252 )
 
conds.append( (bitvecs[24] + bitvecs[5]) == 100 )
 
conds.append( (bitvecs[34] ^ bitvecs[54]) == 2 )
 
conds.append( bitvecs[9] == 54 )
 
conds.append( bitvecs[5] == 50 )
 
conds.append( bitvecs[26] == 49 )
 
conds.append( bitvecs[60] == 50 )
 
conds.append( (bitvecs[4] + bitvecs[7]) == 223 )
 
conds.append( bitvecs[31] == 52 )
 
conds.append( (bitvecs[50] ^ bitvecs[52]) == 0x59 )
 
conds.append( bitvecs[58] == 57 )
 
conds.append( (bitvecs[12] ^ bitvecs[43]) == 0x53 )
 
conds.append( bitvecs[7] == 97 )
 
conds.append( (bitvecs[53] ^ bitvecs[7]) == 0x54 )
 
conds.append( (bitvecs[59] + bitvecs[6]) == 106 )
 
conds.append( (bitvecs[17] + bitvecs[28]) == 110 )
 
conds.append( bitvecs[4] == 123 )
 
conds.append( bitvecs[35] == 101 )
 
conds.append( (bitvecs[36] + bitvecs[44]) == 150 )
 
conds.append( bitvecs[63] == 125 )
 
conds.append( (bitvecs[27] ^ bitvecs[41]) == 0x5D )
 
conds.append( bitvecs[40] == 98 )
 
conds.append( (bitvecs[24] ^ bitvecs[21]) == 0x63 )
 
conds.append( (bitvecs[21] ^ bitvecs[19]) == 0x52 )
 
conds.append( bitvecs[10] == 49 )
 
conds.append( (bitvecs[37] + bitvecs[6]) == 103 )
 
conds.append( bitvecs[6] == 123 )
 
conds.append( bitvecs[56] == 147 )
 
conds.append( (bitvecs[9] ^ bitvecs[29]) == 3 )
 
conds.append( bitvecs[47] == 199 )
 
conds.append( bitvecs[29] == 53 )
 
conds.append( bitvecs[63] == 125 )
 
conds.append( (bitvecs[51] + bitvecs[38]) == 71 )
 
conds.append( (bitvecs[60] + bitvecs[20]) == 147 )
 
conds.append( (bitvecs[1] ^ bitvecs[15]) == 0x74 )
 
conds.append( (bitvecs[11] ^ bitvecs[58]) == 0x16 )
 
conds.append( bitvecs[50] == 49 )
 
conds.append( (bitvecs[0] + bitvecs[63]) == 205 )
 
conds.append( bitvecs[60] == 50 )
 
conds.append( bitvecs[54] == 99 )
 
conds.append( bitvecs[7] == 75 )
 
conds.append( (bitvecs[29] ^ bitvecs[40]) == 0x57 )
 
conds.append( bitvecs[58] == 57 )
 
conds.append( (bitvecs[33] ^ bitvecs[44]) == 0x56 )
 
conds.append( bitvecs[17] == 150 )
 
conds.append( bitvecs[19] == 171 )
 
conds.append( (bitvecs[59] + bitvecs[51]) == 175 )
 
conds.append( bitvecs[21] == 127 )
 
conds.append( (bitvecs[35] ^ bitvecs[11]) == 0xD1 )
 
conds.append( bitvecs[40] == 98 )
 
conds.append( (bitvecs[18] ^ bitvecs[13]) == 0x5E )
 
conds.append( bitvecs[7] == 22 )
 
conds.append( (bitvecs[54] + bitvecs[6]) == 151 )
 
conds.append( bitvecs[50] == 49 )
 
conds.append( bitvecs[45] == 55 )
 
conds.append( (bitvecs[19] + bitvecs[5]) == 104 )
 
conds.append( bitvecs[4] == 26 )
 
conds.append( bitvecs[62] == 48 )
 
conds.append( (bitvecs[12] ^ bitvecs[24]) == 4 )
 
conds.append( (bitvecs[46] + bitvecs[32]) == 150 )
 
conds.append( bitvecs[34] == 97 )
 
conds.append( bitvecs[3] == 70 )
 
conds.append( (bitvecs[11] + bitvecs[47]) == 151 )
 
conds.append( bitvecs[46] == 50 )
 
conds.append( bitvecs[25] == 96 )
 
conds.append( bitvecs[9] == 54 )
 
conds.append( bitvecs[26] == 58 )
 
conds.append( (bitvecs[55] ^ bitvecs[42]) == 0xC )
 
conds.append( (bitvecs[34] ^ bitvecs[19]) == 0x57 )
 
conds.append( bitvecs[56] == 97 )
 
conds.append( (bitvecs[43] ^ bitvecs[31]) == 0x51 )
 
conds.append( bitvecs[55] == 53 )
 
conds.append( bitvecs[9] == 169 )
 
conds.append( (bitvecs[46] + bitvecs[3]) == 120 )
 
conds.append( bitvecs[48] == 31 )
 
conds.append( (bitvecs[35] + bitvecs[23]) == 157 )
 
conds.append( bitvecs[36] == 109 )
 
conds.append( (bitvecs[30] ^ bitvecs[28]) == 6 )
 
conds.append( bitvecs[53] == 48 )
 
conds.append( bitvecs[20] == 247 )
 
conds.append( bitvecs[50] == 49 )
 
conds.append( (bitvecs[60] + bitvecs[45]) == 105 )
 
conds.append( (bitvecs[41] ^ bitvecs[12]) == 5 )
 
conds.append( (bitvecs[9] ^ bitvecs[42]) == 0x85 )
 
conds.append( bitvecs[32] == 100 )
 
conds.append( bitvecs[53] == 48 )
 
conds.append( (bitvecs[38] + bitvecs[55]) == 103 )
 
conds.append( bitvecs[32] == bitvecs[13] )
 
conds.append( bitvecs[36] == 50 )
 
conds.append( bitvecs[23] == 155 )
 
conds.append( bitvecs[13] == 100 )
 
conds.append( bitvecs[8] == 49 )
 
conds.append( bitvecs[36] == 50 )
 
conds.append( bitvecs[14] == 195 )
 
conds.append( (bitvecs[41] + bitvecs[21]) == 151 )
 
conds.append( (bitvecs[45] + bitvecs[37]) == 106 )
 
conds.append( bitvecs[32] == 50 )
 
conds.append( bitvecs[44] == 100 )
 
conds.append( bitvecs[2] == 84 )
 
conds.append( (bitvecs[35] ^ bitvecs[50]) == 0x54 )
 
conds.append( bitvecs[51] == 50 )
 
conds.append( bitvecs[48] == 53 )
 
conds.append( bitvecs[41] == 51 )
 
conds.append( bitvecs[27] == 50 )
 
conds.append( (bitvecs[49] + bitvecs[59]) == 151 )
 
conds.append( bitvecs[36] == 50 )
 
conds.append( bitvecs[22] == 97 )
 
conds.append( (bitvecs[55] + bitvecs[4]) == 18 )
 
conds.append( bitvecs[46] == 158 )
 
conds.append( (bitvecs[22] ^ bitvecs[31]) == 0x55 )
 
conds.append( bitvecs[50] == 67 )
 
conds.append( bitvecs[23] == 56 )
 
conds.append( bitvecs[52] == 12 )
 
conds.append( bitvecs[52] == 48 )
 
conds.append( bitvecs[22] == 97 )
 
conds.append( bitvecs[14] == 54 )
 
conds.append( bitvecs[2] == 84 )
 
conds.append( (bitvecs[8] ^ bitvecs[22]) == 0x50 )
 
conds.append( (bitvecs[35] + bitvecs[0]) == 167 )
 
conds.append( (bitvecs[39] + bitvecs[2]) == 199 )
 
conds.append( (bitvecs[41] ^ bitvecs[6]) == 7 )
 
conds.append( (bitvecs[33] + bitvecs[11]) == 165 )
 
conds.append( bitvecs[25] == 98 )
 
conds.append( bitvecs[26] == 49 )
 
conds.append( (bitvecs[20] + bitvecs[27]) == 35 )
 
conds.append( (bitvecs[6] ^ bitvecs[35]) == 0x9C )
 
conds.append( (bitvecs[14] ^ bitvecs[11]) == 4 )
 
conds.append( bitvecs[39] == 52 )
 
conds.append( (bitvecs[40] + bitvecs[31]) == 150 )
 
conds.append( bitvecs[57] == 99 )
 
conds.append( bitvecs[7] == 100 )
 
conds.append( bitvecs[14] == 54 )
 
conds.append( bitvecs[5] == 67 )
 
conds.append( (bitvecs[23] ^ bitvecs[22]) == 0x59 )
 
conds.append( bitvecs[21] == 100 )
 
conds.append( (bitvecs[22] ^ bitvecs[44]) == 5 )
 
conds.append( bitvecs[53] == 48 )
 
conds.append( bitvecs[31] == 52 )
 
conds.append( bitvecs[22] == 97 )
 
conds.append( (bitvecs[46] + bitvecs[8]) == 122 )
 
conds.append( (bitvecs[25] ^ bitvecs[3]) == 0x24 )
 
conds.append( bitvecs[43] == 101 )
 
conds.append( bitvecs[44] == 15 )
 
conds.append( (bitvecs[16] ^ bitvecs[21]) == 0x57 )
 
conds.append( (bitvecs[9] ^ bitvecs[62]) == 6 )
 
conds.append( bitvecs[27] == 50 )
 
conds.append( (bitvecs[18] + bitvecs[54]) == 209 )
 
conds.append( bitvecs[32] == 100 )
 
conds.append( (bitvecs[57] + bitvecs[18]) == 199 )
 
conds.append( (bitvecs[43] ^ bitvecs[32]) == 1 )
 
conds.append( bitvecs[17] == 164 )
 
conds.append( (bitvecs[8] ^ bitvecs[9]) == 7 )
 
conds.append( bitvecs[40] == 98 )
 
conds.append( (bitvecs[56] + bitvecs[4]) == 10 )
 
conds.append( (bitvecs[21] + bitvecs[28]) == 153 )
 
conds.append( bitvecs[12] == 124 )
 
conds.append( (bitvecs[63] + bitvecs[18]) == 225 )
 
conds.append( bitvecs[27] == 50 )
 
conds.append( bitvecs[23] == 56 )
 
conds.append( (bitvecs[44] + bitvecs[18]) == 200 )
 
conds.append( (bitvecs[9] + bitvecs[19]) == 108 )
 
conds.append( (bitvecs[61] + bitvecs[11]) == 231 )
 
conds.append( bitvecs[21] == 100 )
 
conds.append( (bitvecs[57] + bitvecs[31]) == 151 )
 
conds.append( (bitvecs[28] ^ bitvecs[40]) == 0x57 )
 
conds.append( bitvecs[45] == 55 )
 
conds.append( (bitvecs[13] + bitvecs[47]) == 201 )
 
conds.append( bitvecs[18] == 100 )
 
conds.append( bitvecs[15] == 55 )
 
conds.append( (bitvecs[58] ^ bitvecs[16]) == 0xA )
 
conds.append( (bitvecs[0] ^ bitvecs[21]) == 0x34 )
 
conds.append( (bitvecs[62] + bitvecs[49]) == 145 )
 
conds.append( bitvecs[46] == 50 )
 
conds.append( (bitvecs[57] + bitvecs[0]) == 168 )
 
conds.append( bitvecs[36] == 50 )
 
conds.append( bitvecs[50] == 49 )
 
conds.append( bitvecs[48] == 53 )
 
conds.append( bitvecs[42] == 57 )
 
conds.append( (bitvecs[61] + bitvecs[35]) == 149 )
 
conds.append( (bitvecs[27] + bitvecs[1]) == 117 )
 
conds.append( bitvecs[48] == 53 )
 
conds.append( (bitvecs[35] ^ bitvecs[33]) == 0x51 )
 
conds.append( (bitvecs[29] ^ bitvecs[57]) == 0x56 )
 
conds.append( bitvecs[23] == 75 )
 
conds.append( (bitvecs[31] + bitvecs[13]) == 172 )
 
conds.append( bitvecs[39] == 74 )
 
conds.append( bitvecs[39] == 52 )
 
conds.append( bitvecs[33] == 115 )
 
conds.append( bitvecs[7] == 100 )
 
conds.append( bitvecs[0] == 80 )
 
conds.append( bitvecs[22] == 97 )
 
conds.append( (bitvecs[62] + bitvecs[55]) == 101 )
 
conds.append( bitvecs[52] == 48 )
 
conds.append( (bitvecs[7] + bitvecs[22]) == 204 )
 
conds.append( (bitvecs[26] ^ bitvecs[14]) == 7 )
 
conds.append( bitvecs[2] == 84 )
 
conds.append( bitvecs[46] == 50 )
 
conds.append( bitvecs[52] == 48 )
 
conds.append( (bitvecs[54] ^ bitvecs[35]) == 6 )
 
conds.append( (bitvecs[31] ^ bitvecs[34]) == 0x55 )
 
conds.append( bitvecs[33] == 50 )
 
conds.append( (bitvecs[40] + bitvecs[33]) == 148 )
 
conds.append( bitvecs[7] == 100 )
 
conds.append( bitvecs[15] == 55 )
 
conds.append( (bitvecs[10] ^ bitvecs[43]) == 0x54 )
 
conds.append( bitvecs[15] == 55 )
 
conds.append( (bitvecs[29] + bitvecs[30]) == 104 )
 
conds.append( (bitvecs[43] ^ bitvecs[13]) == 1 )
 
conds.append( (bitvecs[58] + bitvecs[24]) == 217 )
 
conds.append( (bitvecs[17] + bitvecs[61]) == 105 )
 
conds.append( bitvecs[41] == 166 )
 
conds.append( (bitvecs[54] ^ bitvecs[24]) == 0x51 )
 
conds.append( bitvecs[62] == 48 )
 
conds.append( (bitvecs[57] + bitvecs[37]) == 150 )
 
conds.append( (bitvecs[61] ^ bitvecs[4]) == 0x4B )
 
conds.append( (bitvecs[37] + bitvecs[52]) == 99 )
 
conds.append( (bitvecs[21] ^ bitvecs[26]) == 0x3D )
 
conds.append( bitvecs[50] == 233 )
 
conds.append( (bitvecs[5] ^ bitvecs[29]) == 7 )
 
conds.append( bitvecs[31] == 52 )
 
conds.append( bitvecs[53] == 1 )
 
conds.append( (bitvecs[15] + bitvecs[7]) == 155 )
 
conds.append( bitvecs[41] == 51 )
 
conds.append( (bitvecs[35] + bitvecs[27]) == 151 )
 
conds.append( bitvecs[42] == 57 )
 
conds.append( bitvecs[27] == 50 )
 
conds.append( bitvecs[47] == 101 )
 
conds.append( (bitvecs[45] ^ bitvecs[30]) == 4 )
 
conds.append( bitvecs[30] == 51 )
 
conds.append( bitvecs[22] == 97 )
 
conds.append( bitvecs[49] == 97 )
 
conds.append( (bitvecs[31] + bitvecs[21]) == 152 )
 
conds.append( bitvecs[24] == 50 )
 
conds.append( bitvecs[15] == 55 )
 
conds.append( bitvecs[35] == 203 )
 
conds.append( (bitvecs[4] + bitvecs[37]) == 174 )
 
conds.append( bitvecs[49] == 97 )
 
conds.append( (bitvecs[7] ^ bitvecs[31]) == 0x50 )
 
conds.append( (bitvecs[15] + bitvecs[19]) == 109 )
 
conds.append( (bitvecs[30] ^ bitvecs[22]) == 0xC7 )
 
conds.append( (bitvecs[16] ^ bitvecs[60]) == 1 )
 
conds.append( bitvecs[12] == 54 )
 
conds.append( bitvecs[28] == 1 )
 
conds.append( (bitvecs[44] + bitvecs[58]) == 157 )
 
conds.append( (bitvecs[49] ^ bitvecs[37]) == 0x52 )
 
conds.append( bitvecs[6] == 52 )
 
conds.append( bitvecs[38] == 50 )
 
conds.append( bitvecs[62] == 48 )
 
conds.append( (bitvecs[37] ^ bitvecs[21]) == 0x57 )
 
conds.append( (bitvecs[40] + bitvecs[5]) == 148 )
 
conds.append( (bitvecs[11] + bitvecs[34]) == 147 )
 
conds.append( bitvecs[43] == 153 )
 
conds.append( (bitvecs[22] + bitvecs[27]) == 136 )
 
conds.append( bitvecs[46] == bitvecs[38] )
 
conds.append( (bitvecs[48] ^ bitvecs[61]) == 5 )
 
conds.append( bitvecs[12] == 86 )
 
conds.append( (bitvecs[44] ^ bitvecs[28]) == 0x51 )
 
conds.append( bitvecs[45] == 55 )
 
conds.append( (bitvecs[37] ^ bitvecs[2]) == 0x67 )
 
conds.append( (bitvecs[54] ^ bitvecs[16]) == 0x7B )
 
conds.append( (bitvecs[45] ^ bitvecs[18]) == 0x91 )
 
conds.append( bitvecs[18] == 100 )
 