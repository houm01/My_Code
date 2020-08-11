# $language = "python"
# $interface = "1.0"

# This automatically generated script may need to be
# edited in order to work correctly.


def Main():
	crt.Screen.Synchronous = True
	crt.Screen.WaitForString(">")
	crt.Screen.Send("shell" + chr(13))
	crt.Screen.WaitForString("username@example")
	crt.Screen.Send("ssh root@10.1.1.1" + chr(13))
	crt.Screen.WaitForString("Password:")
	crt.Screen.Send("test_password" + chr(13))

Main()
