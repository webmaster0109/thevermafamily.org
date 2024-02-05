from django.contrib.sitemaps import Sitemap

class StaticSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        # List the URLs of your static pages here
        return ['', 'about-us', 'late-shrikant-verma', 'veena-verma', 'abhishek-verma', 'anca-verma', 'nicolle-verma', 'contact-us']

    def location(self, item):
        # Assuming your static pages are at the root level
        return f'/{item}'