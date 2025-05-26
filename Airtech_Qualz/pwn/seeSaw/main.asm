
main:     file format elf64-x86-64


Disassembly of section .init:

0000000000401000 <_init>:
  401000:	48 83 ec 08          	sub    $0x8,%rsp
  401004:	48 8b 05 d5 2f 00 00 	mov    0x2fd5(%rip),%rax        # 403fe0 <__gmon_start__@Base>
  40100b:	48 85 c0             	test   %rax,%rax
  40100e:	74 02                	je     401012 <_init+0x12>
  401010:	ff d0                	call   *%rax
  401012:	48 83 c4 08          	add    $0x8,%rsp
  401016:	c3                   	ret

Disassembly of section .plt:

0000000000401020 <_ZNKSt9basic_iosIcSt11char_traitsIcEE4failEv@plt-0x10>:
  401020:	ff 35 ca 2f 00 00    	push   0x2fca(%rip)        # 403ff0 <_GLOBAL_OFFSET_TABLE_+0x8>
  401026:	ff 25 cc 2f 00 00    	jmp    *0x2fcc(%rip)        # 403ff8 <_GLOBAL_OFFSET_TABLE_+0x10>
  40102c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000401030 <_ZNKSt9basic_iosIcSt11char_traitsIcEE4failEv@plt>:
  401030:	ff 25 ca 2f 00 00    	jmp    *0x2fca(%rip)        # 404000 <_ZNKSt9basic_iosIcSt11char_traitsIcEE4failEv@GLIBCXX_3.4>
  401036:	68 00 00 00 00       	push   $0x0
  40103b:	e9 e0 ff ff ff       	jmp    401020 <_init+0x20>

0000000000401040 <setvbuf@plt>:
  401040:	ff 25 c2 2f 00 00    	jmp    *0x2fc2(%rip)        # 404008 <setvbuf@GLIBC_2.2.5>
  401046:	68 01 00 00 00       	push   $0x1
  40104b:	e9 d0 ff ff ff       	jmp    401020 <_init+0x20>

0000000000401050 <_ZNSi7getlineEPcl@plt>:
  401050:	ff 25 ba 2f 00 00    	jmp    *0x2fba(%rip)        # 404010 <_ZNSi7getlineEPcl@GLIBCXX_3.4>
  401056:	68 02 00 00 00       	push   $0x2
  40105b:	e9 c0 ff ff ff       	jmp    401020 <_init+0x20>

0000000000401060 <_ZNSirsERi@plt>:
  401060:	ff 25 b2 2f 00 00    	jmp    *0x2fb2(%rip)        # 404018 <_ZNSirsERi@GLIBCXX_3.4>
  401066:	68 03 00 00 00       	push   $0x3
  40106b:	e9 b0 ff ff ff       	jmp    401020 <_init+0x20>

0000000000401070 <_ZNSi6ignoreEli@plt>:
  401070:	ff 25 aa 2f 00 00    	jmp    *0x2faa(%rip)        # 404020 <_ZNSi6ignoreEli@GLIBCXX_3.4>
  401076:	68 04 00 00 00       	push   $0x4
  40107b:	e9 a0 ff ff ff       	jmp    401020 <_init+0x20>

0000000000401080 <memcpy@plt>:
  401080:	ff 25 a2 2f 00 00    	jmp    *0x2fa2(%rip)        # 404028 <memcpy@GLIBC_2.14>
  401086:	68 05 00 00 00       	push   $0x5
  40108b:	e9 90 ff ff ff       	jmp    401020 <_init+0x20>

0000000000401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>:
  401090:	ff 25 9a 2f 00 00    	jmp    *0x2f9a(%rip)        # 404030 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@GLIBCXX_3.4>
  401096:	68 06 00 00 00       	push   $0x6
  40109b:	e9 80 ff ff ff       	jmp    401020 <_init+0x20>

00000000004010a0 <_ZNSolsEPFRSoS_E@plt>:
  4010a0:	ff 25 92 2f 00 00    	jmp    *0x2f92(%rip)        # 404038 <_ZNSolsEPFRSoS_E@GLIBCXX_3.4>
  4010a6:	68 07 00 00 00       	push   $0x7
  4010ab:	e9 70 ff ff ff       	jmp    401020 <_init+0x20>

00000000004010b0 <exit@plt>:
  4010b0:	ff 25 8a 2f 00 00    	jmp    *0x2f8a(%rip)        # 404040 <exit@GLIBC_2.2.5>
  4010b6:	68 08 00 00 00       	push   $0x8
  4010bb:	e9 60 ff ff ff       	jmp    401020 <_init+0x20>

Disassembly of section .text:

00000000004010c0 <_start>:
  4010c0:	31 ed                	xor    %ebp,%ebp
  4010c2:	49 89 d1             	mov    %rdx,%r9
  4010c5:	5e                   	pop    %rsi
  4010c6:	48 89 e2             	mov    %rsp,%rdx
  4010c9:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
  4010cd:	50                   	push   %rax
  4010ce:	54                   	push   %rsp
  4010cf:	45 31 c0             	xor    %r8d,%r8d
  4010d2:	31 c9                	xor    %ecx,%ecx
  4010d4:	48 c7 c7 ca 15 40 00 	mov    $0x4015ca,%rdi
  4010db:	ff 15 f7 2e 00 00    	call   *0x2ef7(%rip)        # 403fd8 <__libc_start_main@GLIBC_2.34>
  4010e1:	f4                   	hlt
  4010e2:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
  4010e9:	00 00 00 
  4010ec:	0f 1f 40 00          	nopl   0x0(%rax)

00000000004010f0 <_dl_relocate_static_pie>:
  4010f0:	c3                   	ret
  4010f1:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
  4010f8:	00 00 00 
  4010fb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000401100 <deregister_tm_clones>:
  401100:	b8 58 40 40 00       	mov    $0x404058,%eax
  401105:	48 3d 58 40 40 00    	cmp    $0x404058,%rax
  40110b:	74 13                	je     401120 <deregister_tm_clones+0x20>
  40110d:	b8 00 00 00 00       	mov    $0x0,%eax
  401112:	48 85 c0             	test   %rax,%rax
  401115:	74 09                	je     401120 <deregister_tm_clones+0x20>
  401117:	bf 58 40 40 00       	mov    $0x404058,%edi
  40111c:	ff e0                	jmp    *%rax
  40111e:	66 90                	xchg   %ax,%ax
  401120:	c3                   	ret
  401121:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
  401128:	00 00 00 00 
  40112c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000401130 <register_tm_clones>:
  401130:	be 58 40 40 00       	mov    $0x404058,%esi
  401135:	48 81 ee 58 40 40 00 	sub    $0x404058,%rsi
  40113c:	48 89 f0             	mov    %rsi,%rax
  40113f:	48 c1 ee 3f          	shr    $0x3f,%rsi
  401143:	48 c1 f8 03          	sar    $0x3,%rax
  401147:	48 01 c6             	add    %rax,%rsi
  40114a:	48 d1 fe             	sar    $1,%rsi
  40114d:	74 11                	je     401160 <register_tm_clones+0x30>
  40114f:	b8 00 00 00 00       	mov    $0x0,%eax
  401154:	48 85 c0             	test   %rax,%rax
  401157:	74 07                	je     401160 <register_tm_clones+0x30>
  401159:	bf 58 40 40 00       	mov    $0x404058,%edi
  40115e:	ff e0                	jmp    *%rax
  401160:	c3                   	ret
  401161:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
  401168:	00 00 00 00 
  40116c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000401170 <__do_global_dtors_aux>:
  401170:	f3 0f 1e fa          	endbr64
  401174:	80 3d 95 32 00 00 00 	cmpb   $0x0,0x3295(%rip)        # 404410 <completed.0>
  40117b:	75 13                	jne    401190 <__do_global_dtors_aux+0x20>
  40117d:	55                   	push   %rbp
  40117e:	48 89 e5             	mov    %rsp,%rbp
  401181:	e8 7a ff ff ff       	call   401100 <deregister_tm_clones>
  401186:	c6 05 83 32 00 00 01 	movb   $0x1,0x3283(%rip)        # 404410 <completed.0>
  40118d:	5d                   	pop    %rbp
  40118e:	c3                   	ret
  40118f:	90                   	nop
  401190:	c3                   	ret
  401191:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
  401198:	00 00 00 00 
  40119c:	0f 1f 40 00          	nopl   0x0(%rax)

00000000004011a0 <frame_dummy>:
  4011a0:	f3 0f 1e fa          	endbr64
  4011a4:	eb 8a                	jmp    401130 <register_tm_clones>

00000000004011a6 <_Z3impPv>:
  4011a6:	55                   	push   %rbp
  4011a7:	48 89 e5             	mov    %rsp,%rbp
  4011aa:	48 89 7d f8          	mov    %rdi,-0x8(%rbp)
  4011ae:	48 8b 55 f8          	mov    -0x8(%rbp),%rdx
  4011b2:	48 89 d0             	mov    %rdx,%rax
  4011b5:	58                   	pop    %rax
  4011b6:	c3                   	ret
  4011b7:	90                   	nop
  4011b8:	5d                   	pop    %rbp
  4011b9:	c3                   	ret

00000000004011ba <_Z23print_account_statementv>:
  4011ba:	55                   	push   %rbp
  4011bb:	48 89 e5             	mov    %rsp,%rbp
  4011be:	48 83 ec 70          	sub    $0x70,%rsp
  4011c2:	48 8d 05 3b 0e 00 00 	lea    0xe3b(%rip),%rax        # 402004 <_IO_stdin_used+0x4>
  4011c9:	48 89 c6             	mov    %rax,%rsi
  4011cc:	48 8d 05 ed 2e 00 00 	lea    0x2eed(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  4011d3:	48 89 c7             	mov    %rax,%rdi
  4011d6:	e8 b5 fe ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  4011db:	48 8b 15 ee 2d 00 00 	mov    0x2dee(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  4011e2:	48 89 d6             	mov    %rdx,%rsi
  4011e5:	48 89 c7             	mov    %rax,%rdi
  4011e8:	e8 b3 fe ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  4011ed:	48 8d 05 28 0e 00 00 	lea    0xe28(%rip),%rax        # 40201c <_IO_stdin_used+0x1c>
  4011f4:	48 89 c6             	mov    %rax,%rsi
  4011f7:	48 8d 05 c2 2e 00 00 	lea    0x2ec2(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  4011fe:	48 89 c7             	mov    %rax,%rdi
  401201:	e8 8a fe ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  401206:	48 8b 15 c3 2d 00 00 	mov    0x2dc3(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  40120d:	48 89 d6             	mov    %rdx,%rsi
  401210:	48 89 c7             	mov    %rax,%rdi
  401213:	e8 88 fe ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  401218:	48 8d 05 16 0e 00 00 	lea    0xe16(%rip),%rax        # 402035 <_IO_stdin_used+0x35>
  40121f:	48 89 c6             	mov    %rax,%rsi
  401222:	48 8d 05 97 2e 00 00 	lea    0x2e97(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  401229:	48 89 c7             	mov    %rax,%rdi
  40122c:	e8 5f fe ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  401231:	48 8b 15 98 2d 00 00 	mov    0x2d98(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  401238:	48 89 d6             	mov    %rdx,%rsi
  40123b:	48 89 c7             	mov    %rax,%rdi
  40123e:	e8 5d fe ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  401243:	48 8d 05 05 0e 00 00 	lea    0xe05(%rip),%rax        # 40204f <_IO_stdin_used+0x4f>
  40124a:	48 89 c6             	mov    %rax,%rsi
  40124d:	48 8d 05 6c 2e 00 00 	lea    0x2e6c(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  401254:	48 89 c7             	mov    %rax,%rdi
  401257:	e8 34 fe ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  40125c:	48 8b 15 6d 2d 00 00 	mov    0x2d6d(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  401263:	48 89 d6             	mov    %rdx,%rsi
  401266:	48 89 c7             	mov    %rax,%rdi
  401269:	e8 32 fe ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  40126e:	48 8d 05 e9 0d 00 00 	lea    0xde9(%rip),%rax        # 40205e <_IO_stdin_used+0x5e>
  401275:	48 89 c6             	mov    %rax,%rsi
  401278:	48 8d 05 41 2e 00 00 	lea    0x2e41(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  40127f:	48 89 c7             	mov    %rax,%rdi
  401282:	e8 09 fe ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  401287:	48 8b 15 42 2d 00 00 	mov    0x2d42(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  40128e:	48 89 d6             	mov    %rdx,%rsi
  401291:	48 89 c7             	mov    %rax,%rdi
  401294:	e8 07 fe ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  401299:	48 8d 05 cd 0d 00 00 	lea    0xdcd(%rip),%rax        # 40206d <_IO_stdin_used+0x6d>
  4012a0:	48 89 c6             	mov    %rax,%rsi
  4012a3:	48 8d 05 16 2e 00 00 	lea    0x2e16(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  4012aa:	48 89 c7             	mov    %rax,%rdi
  4012ad:	e8 de fd ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  4012b2:	48 8b 15 17 2d 00 00 	mov    0x2d17(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  4012b9:	48 89 d6             	mov    %rdx,%rsi
  4012bc:	48 89 c7             	mov    %rax,%rdi
  4012bf:	e8 dc fd ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  4012c4:	48 8d 05 b4 0d 00 00 	lea    0xdb4(%rip),%rax        # 40207f <_IO_stdin_used+0x7f>
  4012cb:	48 89 c6             	mov    %rax,%rsi
  4012ce:	48 8d 05 eb 2d 00 00 	lea    0x2deb(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  4012d5:	48 89 c7             	mov    %rax,%rdi
  4012d8:	e8 b3 fd ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  4012dd:	48 8b 15 ec 2c 00 00 	mov    0x2cec(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  4012e4:	48 89 d6             	mov    %rdx,%rsi
  4012e7:	48 89 c7             	mov    %rax,%rdi
  4012ea:	e8 b1 fd ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  4012ef:	48 8d 05 9a 0d 00 00 	lea    0xd9a(%rip),%rax        # 402090 <_IO_stdin_used+0x90>
  4012f6:	48 89 c6             	mov    %rax,%rsi
  4012f9:	48 8d 05 c0 2d 00 00 	lea    0x2dc0(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  401300:	48 89 c7             	mov    %rax,%rdi
  401303:	e8 88 fd ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  401308:	48 8b 15 c1 2c 00 00 	mov    0x2cc1(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  40130f:	48 89 d6             	mov    %rdx,%rsi
  401312:	48 89 c7             	mov    %rax,%rdi
  401315:	e8 86 fd ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  40131a:	48 8d 05 81 0d 00 00 	lea    0xd81(%rip),%rax        # 4020a2 <_IO_stdin_used+0xa2>
  401321:	48 89 c6             	mov    %rax,%rsi
  401324:	48 8d 05 95 2d 00 00 	lea    0x2d95(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  40132b:	48 89 c7             	mov    %rax,%rdi
  40132e:	e8 5d fd ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  401333:	48 8b 15 96 2c 00 00 	mov    0x2c96(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  40133a:	48 89 d6             	mov    %rdx,%rsi
  40133d:	48 89 c7             	mov    %rax,%rdi
  401340:	e8 5b fd ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  401345:	e8 cc 02 00 00       	call   401616 <_ZNSt14numeric_limitsIlE3maxEv>
  40134a:	ba 0a 00 00 00       	mov    $0xa,%edx
  40134f:	48 89 c6             	mov    %rax,%rsi
  401352:	48 8d 05 87 2e 00 00 	lea    0x2e87(%rip),%rax        # 4041e0 <_ZSt3cin@GLIBCXX_3.4>
  401359:	48 89 c7             	mov    %rax,%rdi
  40135c:	e8 0f fd ff ff       	call   401070 <_ZNSi6ignoreEli@plt>
  401361:	48 8d 05 4b 0d 00 00 	lea    0xd4b(%rip),%rax        # 4020b3 <_IO_stdin_used+0xb3>
  401368:	48 89 c6             	mov    %rax,%rsi
  40136b:	48 8d 05 4e 2d 00 00 	lea    0x2d4e(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  401372:	48 89 c7             	mov    %rax,%rdi
  401375:	e8 16 fd ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  40137a:	ba 00 10 00 00       	mov    $0x1000,%edx
  40137f:	48 8d 05 9a 30 00 00 	lea    0x309a(%rip),%rax        # 404420 <data>
  401386:	48 89 c6             	mov    %rax,%rsi
  401389:	48 8d 05 50 2e 00 00 	lea    0x2e50(%rip),%rax        # 4041e0 <_ZSt3cin@GLIBCXX_3.4>
  401390:	48 89 c7             	mov    %rax,%rdi
  401393:	e8 b8 fc ff ff       	call   401050 <_ZNSi7getlineEPcl@plt>
  401398:	48 8d 05 51 2e 00 00 	lea    0x2e51(%rip),%rax        # 4041f0 <_ZSt3cin@GLIBCXX_3.4+0x10>
  40139f:	48 89 c7             	mov    %rax,%rdi
  4013a2:	e8 89 fc ff ff       	call   401030 <_ZNKSt9basic_iosIcSt11char_traitsIcEE4failEv@plt>
  4013a7:	84 c0                	test   %al,%al
  4013a9:	74 35                	je     4013e0 <_Z23print_account_statementv+0x226>
  4013ab:	48 8d 05 13 0d 00 00 	lea    0xd13(%rip),%rax        # 4020c5 <_IO_stdin_used+0xc5>
  4013b2:	48 89 c6             	mov    %rax,%rsi
  4013b5:	48 8d 05 44 2f 00 00 	lea    0x2f44(%rip),%rax        # 404300 <_ZSt4cerr@GLIBCXX_3.4>
  4013bc:	48 89 c7             	mov    %rax,%rdi
  4013bf:	e8 cc fc ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  4013c4:	48 8b 15 05 2c 00 00 	mov    0x2c05(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  4013cb:	48 89 d6             	mov    %rdx,%rsi
  4013ce:	48 89 c7             	mov    %rax,%rdi
  4013d1:	e8 ca fc ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  4013d6:	bf 01 00 00 00       	mov    $0x1,%edi
  4013db:	e8 d0 fc ff ff       	call   4010b0 <exit@plt>
  4013e0:	48 8d 45 90          	lea    -0x70(%rbp),%rax
  4013e4:	ba 90 00 00 00       	mov    $0x90,%edx
  4013e9:	48 8d 0d 30 30 00 00 	lea    0x3030(%rip),%rcx        # 404420 <data>
  4013f0:	48 89 ce             	mov    %rcx,%rsi
  4013f3:	48 89 c7             	mov    %rax,%rdi
  4013f6:	e8 85 fc ff ff       	call   401080 <memcpy@plt>
  4013fb:	48 8d 05 d9 0c 00 00 	lea    0xcd9(%rip),%rax        # 4020db <_IO_stdin_used+0xdb>
  401402:	48 89 c6             	mov    %rax,%rsi
  401405:	48 8d 05 b4 2c 00 00 	lea    0x2cb4(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  40140c:	48 89 c7             	mov    %rax,%rdi
  40140f:	e8 7c fc ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  401414:	48 89 c2             	mov    %rax,%rdx
  401417:	48 8d 45 90          	lea    -0x70(%rbp),%rax
  40141b:	48 89 c6             	mov    %rax,%rsi
  40141e:	48 89 d7             	mov    %rdx,%rdi
  401421:	e8 6a fc ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  401426:	48 8b 15 a3 2b 00 00 	mov    0x2ba3(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  40142d:	48 89 d6             	mov    %rdx,%rsi
  401430:	48 89 c7             	mov    %rax,%rdi
  401433:	e8 68 fc ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  401438:	90                   	nop
  401439:	c9                   	leave
  40143a:	c3                   	ret

000000000040143b <_Z10atm_systemv>:
  40143b:	55                   	push   %rbp
  40143c:	48 89 e5             	mov    %rsp,%rbp
  40143f:	48 83 ec 10          	sub    $0x10,%rsp
  401443:	48 8d 05 a3 0c 00 00 	lea    0xca3(%rip),%rax        # 4020ed <_IO_stdin_used+0xed>
  40144a:	48 89 c6             	mov    %rax,%rsi
  40144d:	48 8d 05 6c 2c 00 00 	lea    0x2c6c(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  401454:	48 89 c7             	mov    %rax,%rdi
  401457:	e8 34 fc ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  40145c:	48 8b 15 6d 2b 00 00 	mov    0x2b6d(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  401463:	48 89 d6             	mov    %rdx,%rsi
  401466:	48 89 c7             	mov    %rax,%rdi
  401469:	e8 32 fc ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  40146e:	48 8d 05 81 0c 00 00 	lea    0xc81(%rip),%rax        # 4020f6 <_IO_stdin_used+0xf6>
  401475:	48 89 c6             	mov    %rax,%rsi
  401478:	48 8d 05 41 2c 00 00 	lea    0x2c41(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  40147f:	48 89 c7             	mov    %rax,%rdi
  401482:	e8 09 fc ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  401487:	48 8b 15 42 2b 00 00 	mov    0x2b42(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  40148e:	48 89 d6             	mov    %rdx,%rsi
  401491:	48 89 c7             	mov    %rax,%rdi
  401494:	e8 07 fc ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  401499:	48 8d 05 70 0c 00 00 	lea    0xc70(%rip),%rax        # 402110 <_IO_stdin_used+0x110>
  4014a0:	48 89 c6             	mov    %rax,%rsi
  4014a3:	48 8d 05 16 2c 00 00 	lea    0x2c16(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  4014aa:	48 89 c7             	mov    %rax,%rdi
  4014ad:	e8 de fb ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  4014b2:	48 8b 15 17 2b 00 00 	mov    0x2b17(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  4014b9:	48 89 d6             	mov    %rdx,%rsi
  4014bc:	48 89 c7             	mov    %rax,%rdi
  4014bf:	e8 dc fb ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  4014c4:	48 8d 05 56 0c 00 00 	lea    0xc56(%rip),%rax        # 402121 <_IO_stdin_used+0x121>
  4014cb:	48 89 c6             	mov    %rax,%rsi
  4014ce:	48 8d 05 eb 2b 00 00 	lea    0x2beb(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  4014d5:	48 89 c7             	mov    %rax,%rdi
  4014d8:	e8 b3 fb ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  4014dd:	48 8b 15 ec 2a 00 00 	mov    0x2aec(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  4014e4:	48 89 d6             	mov    %rdx,%rsi
  4014e7:	48 89 c7             	mov    %rax,%rdi
  4014ea:	e8 b1 fb ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  4014ef:	48 8d 05 3d 0c 00 00 	lea    0xc3d(%rip),%rax        # 402133 <_IO_stdin_used+0x133>
  4014f6:	48 89 c6             	mov    %rax,%rsi
  4014f9:	48 8d 05 c0 2b 00 00 	lea    0x2bc0(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  401500:	48 89 c7             	mov    %rax,%rdi
  401503:	e8 88 fb ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  401508:	48 8d 45 fc          	lea    -0x4(%rbp),%rax
  40150c:	48 89 c6             	mov    %rax,%rsi
  40150f:	48 8d 05 ca 2c 00 00 	lea    0x2cca(%rip),%rax        # 4041e0 <_ZSt3cin@GLIBCXX_3.4>
  401516:	48 89 c7             	mov    %rax,%rdi
  401519:	e8 42 fb ff ff       	call   401060 <_ZNSirsERi@plt>
  40151e:	8b 45 fc             	mov    -0x4(%rbp),%eax
  401521:	83 f8 03             	cmp    $0x3,%eax
  401524:	74 48                	je     40156e <_Z10atm_systemv+0x133>
  401526:	83 f8 03             	cmp    $0x3,%eax
  401529:	7f 70                	jg     40159b <_Z10atm_systemv+0x160>
  40152b:	83 f8 01             	cmp    $0x1,%eax
  40152e:	74 07                	je     401537 <_Z10atm_systemv+0xfc>
  401530:	83 f8 02             	cmp    $0x2,%eax
  401533:	74 0c                	je     401541 <_Z10atm_systemv+0x106>
  401535:	eb 64                	jmp    40159b <_Z10atm_systemv+0x160>
  401537:	e8 7e fc ff ff       	call   4011ba <_Z23print_account_statementv>
  40153c:	e9 86 00 00 00       	jmp    4015c7 <_Z10atm_systemv+0x18c>
  401541:	48 8d 05 fe 0b 00 00 	lea    0xbfe(%rip),%rax        # 402146 <_IO_stdin_used+0x146>
  401548:	48 89 c6             	mov    %rax,%rsi
  40154b:	48 8d 05 6e 2b 00 00 	lea    0x2b6e(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  401552:	48 89 c7             	mov    %rax,%rdi
  401555:	e8 36 fb ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  40155a:	48 8b 15 6f 2a 00 00 	mov    0x2a6f(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  401561:	48 89 d6             	mov    %rdx,%rsi
  401564:	48 89 c7             	mov    %rax,%rdi
  401567:	e8 34 fb ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  40156c:	eb 59                	jmp    4015c7 <_Z10atm_systemv+0x18c>
  40156e:	48 8d 05 e5 0b 00 00 	lea    0xbe5(%rip),%rax        # 40215a <_IO_stdin_used+0x15a>
  401575:	48 89 c6             	mov    %rax,%rsi
  401578:	48 8d 05 41 2b 00 00 	lea    0x2b41(%rip),%rax        # 4040c0 <_ZSt4cout@GLIBCXX_3.4>
  40157f:	48 89 c7             	mov    %rax,%rdi
  401582:	e8 09 fb ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  401587:	48 8b 15 42 2a 00 00 	mov    0x2a42(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  40158e:	48 89 d6             	mov    %rdx,%rsi
  401591:	48 89 c7             	mov    %rax,%rdi
  401594:	e8 07 fb ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  401599:	eb 2c                	jmp    4015c7 <_Z10atm_systemv+0x18c>
  40159b:	48 8d 05 cd 0b 00 00 	lea    0xbcd(%rip),%rax        # 40216f <_IO_stdin_used+0x16f>
  4015a2:	48 89 c6             	mov    %rax,%rsi
  4015a5:	48 8d 05 54 2d 00 00 	lea    0x2d54(%rip),%rax        # 404300 <_ZSt4cerr@GLIBCXX_3.4>
  4015ac:	48 89 c7             	mov    %rax,%rdi
  4015af:	e8 dc fa ff ff       	call   401090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
  4015b4:	48 8b 15 15 2a 00 00 	mov    0x2a15(%rip),%rdx        # 403fd0 <_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_@GLIBCXX_3.4>
  4015bb:	48 89 d6             	mov    %rdx,%rsi
  4015be:	48 89 c7             	mov    %rax,%rdi
  4015c1:	e8 da fa ff ff       	call   4010a0 <_ZNSolsEPFRSoS_E@plt>
  4015c6:	90                   	nop
  4015c7:	90                   	nop
  4015c8:	c9                   	leave
  4015c9:	c3                   	ret

00000000004015ca <main>:
  4015ca:	55                   	push   %rbp
  4015cb:	48 89 e5             	mov    %rsp,%rbp
  4015ce:	48 8b 05 bb 2a 00 00 	mov    0x2abb(%rip),%rax        # 404090 <stdin@GLIBC_2.2.5>
  4015d5:	b9 00 00 00 00       	mov    $0x0,%ecx
  4015da:	ba 00 00 00 00       	mov    $0x0,%edx
  4015df:	be 00 00 00 00       	mov    $0x0,%esi
  4015e4:	48 89 c7             	mov    %rax,%rdi
  4015e7:	e8 54 fa ff ff       	call   401040 <setvbuf@plt>
  4015ec:	48 8b 05 8d 2a 00 00 	mov    0x2a8d(%rip),%rax        # 404080 <stdout@GLIBC_2.2.5>
  4015f3:	b9 00 00 00 00       	mov    $0x0,%ecx
  4015f8:	ba 00 00 00 00       	mov    $0x0,%edx
  4015fd:	be 00 00 00 00       	mov    $0x0,%esi
  401602:	48 89 c7             	mov    %rax,%rdi
  401605:	e8 36 fa ff ff       	call   401040 <setvbuf@plt>
  40160a:	e8 2c fe ff ff       	call   40143b <_Z10atm_systemv>
  40160f:	b8 00 00 00 00       	mov    $0x0,%eax
  401614:	5d                   	pop    %rbp
  401615:	c3                   	ret

0000000000401616 <_ZNSt14numeric_limitsIlE3maxEv>:
  401616:	55                   	push   %rbp
  401617:	48 89 e5             	mov    %rsp,%rbp
  40161a:	48 b8 ff ff ff ff ff 	movabs $0x7fffffffffffffff,%rax
  401621:	ff ff 7f 
  401624:	5d                   	pop    %rbp
  401625:	c3                   	ret

Disassembly of section .fini:

0000000000401628 <_fini>:
  401628:	48 83 ec 08          	sub    $0x8,%rsp
  40162c:	48 83 c4 08          	add    $0x8,%rsp
  401630:	c3                   	ret
