#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   sushiting
#   E-mail  :   sushiting@163.com
#   Date    :   13/08/05 15:26:14
#   Desc    :   
#
import SocketServer
class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.data = self.request.recv(1024).strip()
		print "{} wrote:".format(self.client_address[0])
		print self.data
		self.request.sendall(self.data.upper())
