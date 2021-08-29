import _100_RandomPassword
import _102_checkpassword



conteggio = 0
password_ok = False
while password_ok != True:
 stringa = _100_RandomPassword.RandomPassword()
 password_ok =_102_checkpassword.Controllopassword(stringa)
 conteggio += 1
 





print(conteggio)

