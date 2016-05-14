# encoding: utf-8
#!/usr/bin/python 
import paramiko
 
t = paramiko.Transport('10.10.16.42','22')
t.connect(username = 'root', password = '123456')
sftp = paramiko.SFTPClient.from_transport(t)
remotepath='/yt/tmp/test.log'
localpath='d:/Temp/ssh/tmp/test2.log'
sftp.get(remotepath, localpath)
sftp.put('d:/Temp/ssh/testSFTP.txt','/yt/tmp/sftpTest.txt')
t.close()