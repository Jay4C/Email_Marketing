import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from socket import gaierror


def email_marketing_with_one_attachment(username_1, password_1, prenom_1, nom_1, telephone_1, filename_1, poste_1):
    fromaddr = username_1
    password = password_1

    # temporary employment agencies in Paris (75)
    emails = [
        'contact@adecco.fr',
        'contact@coburngroup.fr',
        'contact@sovitrat.fr',
        'contact@interaction-interim.com',
        'contact@startpeople.fr',
        'contact@brigad.co',
        'contact@qapa.com',
        'contact@rhsante.fr',
        'contact@horscliches.com',
        'contact@groupeactual.eu',
        'contact@gif.fr',
        'contact@leboncandidat.fr',
        'contact@ergalis.fr',
        'contact@evs.fr',
        'contact@ras-interim.fr',
        'contact@modelor.fr',
        'contact@jobberry.com',
        'contact@cameleonsrh.com',
        'contact@sfr.fr',
        'contact@eurobtp.fr',
        'contact@netquarks.com',
        'contact@randstad.fr',
        'contact@randstad-direct.fr',
        'contact@kellyservices.fr',
        'contact@ots.fr',
        'contact@quickinterim.com',
        'contact@lfpinterim.com',
        'contact@progressis.com',
        'contact@tercio-rh.com',
        'contact@groupedlsi.com',
        'contact@proman-interim.com',
        'contact@fashion-expert.fr',
        'contact@groupe-sfrh.com',
        'contact@samsic-emploi.fr',
        'contact@groupe-crit.com',
        'contact@agemsante.com',
        'contact@skills-rh.fr',
        'contact@kobaltt.com',
        'contact@groupe-minerve.eu',
        'contact@selectively.co',
        'contact@adeccomedical.fr',
        'contact@sli-interim.fr',
        'contact@appel-medical.com',
        'contact@oradeo.com',
        'contact@allo-medic.com',
        'contact@interim-nation.fr',
        'contact@rs-interim.fr',
        'contact@sads-interim.eu',
        'contact@industrie-interim.fr',
        'contact@partnaire.fr',
        'contact@acp-interim.fr',
        'contact@emploilib.fr',
        'contact@wanadoo.fr',
        'contact@axxisressources.fr',
        'contact@orange.fr',
        'contact@gmail.com',
        'contact@yahoo.fr',
        'contact@rhezo-interim.fr',
        'contact@assistance-interim.fr',
        'contact@dominointerim.com',
        'contact@lipinterim.fr',
        'contact@expertive.fr',
        'contact@connectt.fr',
        'contact@teamexpert.fr',
        'contact@imancorp.fr',
        'contact@delco-emploi.fr',
        'contact@dynamis-rh.com',
        'contact@j4s.fr',
        'contact@mecatrans.fr',
        'contact@initialrh.fr',
        'contact@ekorsinterim.fr',
        'contact@magic.fr',
        'contact@appelmedicalsearch.com',
        'contact@dlh-planett.fr',
        'contact@instead.fr',
        'contact@stylma.fr',
        'contact@rinterim.fr',
        'contact@egekip-rh.fr',
        'contact@dpsinterim.fr',
        'contact@asemploi.fr',
        'contact@cdme.fr',
        'contact@jacem.fr',
        'contact@esperia-ett.fr',
        'contact@next-terra.com',
        'contact@jti-finance.fr',
        'contact@jober.paris',
        'contact@lynx-rh.com',
        'contact@williamsinclair.com',
        'contact@scientechinterim.com',
        'contact@walterspeople.com',
        'contact@temporis.fr',
        'contact@adecco-pme.fr',
        'contact@globe-interim.fr',
        'contact@swisslog.com',
        'contact@wing.eu',
        'contact@essor92.fr',
        'contact@eventlogistic.fr',
        'contact@synergie.fr',
        'contact@bestshore.fr',
        'contact@roberthalf.fr',
        'contact@betech.fr',
        'contact@social-and-co.fr',
        'contact@tempus-interim.com',
        'contact@abalone-interim.com',
        'contact@menway-interim.fr',
        'contact@chrono-interim.fr',
        'contact@klesia.fr',
        'contact@ses-interim.fr',
        'contact@ihl.fr',
        'contact@groupeadequat.fr',
        'contact@fhinterim.fr',
        'contact@arianeinterim.fr',
        'contact@amaris-interim.com',
        'contact@alerys.fr',
        'contact@recrutement-hotellerie-restauration.com'
    ]

    prenom = prenom_1
    nom = nom_1
    telephone = telephone_1

    body = (
        "Bonjour,\n\n"
        "Je suis à la recherche d'un poste de " + poste_1 + " en CDI.\n"
        "Veuillez trouver mon CV en pièce jointe.\n\n"
        "Bien cordialement, \n\n" +
        prenom + " " + nom + "\n" +
        "Téléphone : " + telephone
    )

    filename = filename_1
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    "attachment; filename= %s" % filename)

    for email in emails:
        toaddr = email
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Candidature spontanée pour un poste de " + poste_1 + " en CDI"

        msg.attach(MIMEText(body, 'plain'))

        msg.attach(part)

        text = msg.as_string()

        try:
            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server_ssl.ehlo()
            server_ssl.login(fromaddr, password)
            server_ssl.sendmail(fromaddr, toaddr, text)
            server_ssl.quit()

        except (gaierror, ConnectionRefusedError):
            # tell the script to report if your message was sent or which errors need to be fixed
            print('Failed to connect to the server. Bad connection settings?')

        except smtplib.SMTPServerDisconnected:
            print('Failed to connect to the server. Wrong user/password?')

        except smtplib.SMTPException as e:
            print('SMTP error occurred: ' + str(e))

        else:
            print('Sent to : ' + str(email))

    attachment.close()

# activate third app setting on your Gmail account to permit to send emails from any apps
email_marketing_with_one_attachment(
    username_1="",
    password_1="",
    prenom_1="",
    nom_1="",
    telephone_1="",
    filename_1="",
    poste_1=""
)
