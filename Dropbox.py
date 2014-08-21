# Include the Dropbox and gnupg SDK 
import dropbox
import gnupg

# Get your app key and secret from the Dropbox developer website
app_key = '358zuto54drzue2'
app_secret = 'acwl43anasg0blc'

# step to start the authorization flow from dropbox
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

# Have the user sign in and authorize this token
authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
#Enter the above link in a web Browser and then enter the authorization code below
code = raw_input("Enter the authorization code here: ").strip()

# This will fail if the user enters an invalid authorization code
access_token, user_id = flow.finish(code)

# linking to the Users Dropbox account
client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()

#filename = raw_input('Enter the filename to be uploaded: ')

# Path of the Gnupg for the signature verification process on your local machine
gpg = gnupg.GPG(gnupghome='C:\Program Files (x86)\GNU\GnuPG')
gpg.encoding = 'utf-8'
print ' GPG:' , gpg


input_data = gpg.gen_key_input(key_type="RSA", key_length=1024)
key = gpg.gen_key(input_data)
private_keys = gpg.list_keys(True)
print private_keys                   


# The path of the file to be read E:\working-draft.txt
f = open('E:\working-draft.txt',"rb")

# Users Key id and other details for the signature verification
keyid='5FE186F872209232'
clearsign='True'
detach='True'
binary='True'

# Getting the signed data and uploading this to dropbox
signed_data = gpg.sign_file(f,keyid,clearsign,detach)

# Printing the Gnupg Signature for the file
print 'Opened the file and trying to sign it.'
print str(signed_data)

# Printing the Response if the file has been uploaded or not
response = client.put_file('/magnum-opus.txt', str(signed_data))
print 'uploaded: ', response

# Meatadata is being printed on the screen
folder_metadata = client.metadata('/')
print 'metadata: ', folder_metadata

#steps to download the file from dropbox and verify it.
print 'Before downloading the file fron dropbox:'
f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
out = open(r'E:\magnum-opus.txt', 'wb')
print 'Reading the downloaded File'

out.write(f.read())
print 'After reading Downloaded File'

# Closing the downoladed file
out.close()
print 'metadata: ', metadata

# Opening the Downloaded file in Read-mode
out1 = open('E:\magnum-opus.txt', "rb")

# Verifiying the Downloaded file.
#verified = gpg.verify_file('L1Q9LouWfRTAZDAa+0Xt9zR1RhY','E:\working-draft.txt')
verified = gpg.verify_file(out1,'E:\working-draft.txt') 
if not verified:
     raise ValueError("Signature could not be verified!")
else:
    print 'Signature was verified.'
    print 'verified.username:',verified.username
    print 'verified.key_id:', verified.key_id
    print 'verified.signature_id :' ,verified.signature_id
    print 'verified.fingerprint:' , verified.fingerprint
    print 'verified.trust_level:', verified.trust_level
    print 'verified.trust_text:' , verified.trust_text

out1.close()

# if not verified Raises an Error.

# End of Program
