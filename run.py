if __name__=='__main__':
	try:
		__import__("Brutes").access_token()
	except Exception as e:
		exit(str(e))