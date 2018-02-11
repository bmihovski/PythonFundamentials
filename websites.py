"""
You have been tasked to create an ordered database of websites. For the task you will need to create a class Website,
which will have a Host, a Domain and Queries.
The Host and the Domain are simple strings.
The Queries, is Collections of strings.
You will be given several input lines in the following format:
{host} | {domain} | {query1,query2. . .}
Note: There will always be a host and a domain, but there might NOT be ANY queries.
The input sequence ends, when you receive the command "end". Then you must print all websites in the following format:
https://www.{host}.{domain}/query?=[{query1]&[{query2}]&[query3]. . .
In case there are NO queries, just print:
https://www.{host}.{domain}

Examples

Input

softuni | bg | user,course,homework
judge.softuni | bg | contest,bg
google | bg | search,query
zamunda | net
end

Output

https://www.softuni.bg/query?=[user]&[course]&[homework]
https://www.judge.softuni.bg/query?=[contest]&[bg]
https://www.google.bg/query?=[search]&[query]
https://www.zamunda.net
"""


class Websites:
    def __init__(self, host, domain_name, queries=None):
        """
        Initialising web site url
        :param host: (Str) Server hostname
        :param domain_name: (Str) Domain name
        :param queries: (Str) Query added to url - default None
        """
        self.host = host
        self.domain_name = domain_name
        self.queries = queries

    def __str__(self):
        """
        Visualise constructed url
        :return: (Str) URL to be represented
        """
        if not self.queries:
            website_record = f'https://www.{self.host}.{self.domain_name}'
        else:
            website_query = ''.join([f'[{item}]&' for item in self.queries[:-1]])
            website_record = f'https://www.{self.host}.{self.domain_name}/query?={website_query}[{self.queries[-1]}]'
        return website_record


input_websites = list()

while True:
    input_texts = input().split(' | ')
    if 'end' in input_texts:
        break
    elif ',' in input_texts[-1]:
        web_queries = input_texts[-1].split(',')
        input_websites.append(Websites(host=input_texts[0], domain_name=input_texts[1], queries=web_queries))
    else:
        input_websites.append(Websites(host=input_texts[0], domain_name=input_texts[1]))

[print(web_query) for web_query in input_websites]
