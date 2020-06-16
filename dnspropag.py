import banner
import collections
import click
import dns.resolver

def print_resolver(dns_server_location, dns_data):
    print("\033[1;34m[+] {0} \t\t\033[0;0m {1}".format(dns_server_location,\
                                                       dns_data))

@click.command()
@click.option('--domain', nargs=1)
@click.option('--dnstype', nargs=1)
def main(domain, dnstype):
    dns_servers = collections.OrderedDict()

    dns_servers['Australia'] = "203.89.226.24"
    dns_servers["Brazil"] = "200.181.14.3"
    dns_servers["Cloudflare"] = "1.1.1.1"
    dns_servers["Chile"] = "200.27.137.187"
    dns_servers["China"] = "202.46.34.75"
    dns_servers["France"] = "188.165.220.211"
    dns_servers["Germany"] = "78.46.231.162"
    dns_servers["Google"] = "8.8.8.8"
    dns_servers["Google"] = "8.8.4.4"
    dns_servers["Japan"] = "101.110.33.227"
    dns_servers["Africa"] = "41.208.16.161"
    dns_servers["USA"] = "199.45.32.43"

    dns_resolver = dns.resolver.Resolver()

    for dns_server_location, dns_server in zip(dns_servers.keys(), \
                                               dns_servers.values()):
                    
        dns_resolver.nameservers = [dns_server]
        try:
            dns_query = dns_resolver.query(domain, dnstype)

            [print_resolver(dns_server_location, dns_data) \
                for dns_data in dns_query]

        except:
            print_resolver(dns_server_location, 'X')        

if __name__=='__main__':
    banner.print_banner()
    main()
