from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        """
        General idea: use a dictionary to store domain name and it's count
        """
        domain_visit = defaultdict(int)
        for cpdomain in cpdomains:
            # cp = '9001', domain = 'discuss.leetcode.com'
            cp, domain = cpdomain.split(' ')
            #subdomains = ['discuss', 'leetcode', 'com']
            subdomains = domain.split('.')
            new_subdomain = ''
            for subdomain in subdomains[::-1]:
                # 'com'
                new_subdomain = subdomain + new_subdomain
                # '9001 com'
                domain_visit[new_subdomain] += int(cp)
                # '.com'
                new_subdomain = '.' + new_subdomain
        return [str(value) + ' '+ key for key, value in domain_visit.items()]