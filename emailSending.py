import smtplib



sender_email = "skunknown7991@gmail.com"
sender_password = 'yduzxebtlmvafodm'

def send_email(to_email, subject, body, cc="", bcc=""):
    # Gmail SMTP server settings
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # TLS port
    
    # Create SMTP connection
    smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
    smtp_conn.ehlo()  # Identify yourself to the SMTP server
    smtp_conn.starttls()  # Enable encryption (TLS)
    smtp_conn.ehlo()  # Re-identify yourself after encryption
    
    # Log in to your Gmail account
    smtp_conn.login(str(sender_email), str(sender_password))
    
    # Compose the email
    email_headers = [
        f'From: {sender_email}',
        f'To: {to_email}',
        f'Subject: {subject}',
    ]
    
    if cc:
        email_headers.append(f'Cc: {cc}')

    if bcc:
        email_headers.append(f'Bcc: {bcc}')
    
    email_headers.extend([
        'MIME-Version: 1.0',
        'Content-Type: text/html'
    ])
    
    email_body = body
    email_ = '\r\n'.join(email_headers + ['', email_body])
    
    # Send the email
    try:
        smtp_conn.sendmail(str(sender_email), [to_email] + ([cc] if cc else []) + ([bcc] if bcc else []), email_)
        smtp_conn.quit()
        return 'Email sent successfully!'
    except Exception as e:
        smtp_conn.quit()
        return f'Failed to send email. Error: {str(e)}'



# updated email func
def sendPostApprovalEmail(toEmail: str,  postTitle:str, poststatus: str, postOwnerUserName: str, cc: str = "SanjeevK@cryptoassetrating.com", bcc: str = "niroge8972@kameili.com"):
    email_body = f"""<html> <head></head> <body> 
        <p>Hi {postOwnerUserName},</p> 
        <p>Your post of postTitle: {postTitle} has been {poststatus} by admin. Please login to see details.</p><br/> 
        <p>Best regards,<br>Crypto Business World</p> </body> </html>"""

    send_email(toEmail,
              f"Post Update Notification",
              email_body.format(postTitle=postTitle, poststatus=poststatus, postOwnerUserName=postOwnerUserName),
              cc=cc,
              bcc=bcc)

    return {"message": "mail sent successfully!"}


x = sendPostApprovalEmail(toEmail="sanjukaushik.1997@gmail.com", postTitle="this is post title",poststatus="", postOwnerUserName="Snajeev", cc="SanjeevK@cryptoassetrating.com")
print("this is x", x)

