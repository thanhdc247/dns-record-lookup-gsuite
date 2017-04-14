import dns.resolver

def lookup_mx(domain_name):
    try:
        answers = dns.resolver.query(domain_name, 'MX')
        mx_records = ['alt1.aspmx.l.google.com.',
                      'alt2.aspmx.l.google.com.',
                      'alt3.aspmx.l.google.com.',
                      'alt4.aspmx.l.google.com.',
                    'aspmx.l.google.com.' ]
        for rdata in answers:
            if str(rdata.exchange) in mx_records:
                return True
            else:
                return False
    except:
        return False

def lookup_spf(domain_name):
    try:
        answers = dns.resolver.query(domain_name, 'TXT')
        spf_google = ['include:_spf.google.com', '~all']
        isSPF = False
        for rdata in answers:
            if str(rdata).startswith('"v=spf1'):
                if spf_google[0] in str(rdata):
                    if spf_google[1] in str(rdata):
                        return True
        return isSPF
    except:
        return False


def lookup_dkim(domain_name):
    try:
        answers = dns.resolver.query('google._domainkey.' + domain_name, 'TXT')
        return True
    except:
        return False


def lookup_dmarc(domain_name):
    try:
        answers = dns.resolver.query('_dmarc.' + domain_name, 'TXT')
        return True
    except:
        return False
