#Script para medir la velocidad de internet:
# Ver la docuemntacion aca: https://pypi.org/project/speedtest-cli/
#Tiene que estar en Python 2.7 o el modulo de mierda no se importa bien.



from decimal import Decimal
import speedtest   
  
st = speedtest.Speedtest() 
  

print "-----------------------------------------------"  
print "Test en proceso: espere un momento por favor... "  
print "-----------------------------------------------"  

clear()

#Tests:
bajada = st.download()
bajada = str(round(bajada / 1000000,2))

subida = st.upload()
subida = str(round(subida / 1000000,2))

ping = str(round(float(st.results.ping),2))
  
  



#Resultados
print "Resultados:"
print "Velocidad de bajada: " + bajada + " Mbits/s"
print "Velocidad de subida: " + subida + " Mbits/s"
print "Ping: " + ping + " ms"  
print "------------ Test finalizado --------------"   
  
