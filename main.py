import webapp2
import jinja2

template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env=jinja2.Environment(loader=template_loader)

def seers(x):
    arr = [22]
    return arr[x]

def sizes(y):
    lis = [24000]
    return lis[y]

def states(z):
    if z == 'tx':
        return 10.98

def avgthese(a, b):
    one = int(a)
    two = int(b)
    sum = one+two
    return sum/2

class HomePage(webapp2.RequestHandler):
    def get(self):
        home_temp = template_env.get_template('templates/home.html')
        self.response.write(home_temp.render())

class RegionPage(webapp2.RequestHandler):
    def get(self):
        region_template = template_env.get_template('templates/region.html')
        self.response.write(region_template.render())

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        min = self.request.get('mintemp')
        max = self.request.get('maxtemp')
        avg = avgthese(min, max)
        regavg = 69.95
        stavg = 69.9
        if avg < stavg:
            diff = stavg - avg
            diffst = 'Your household setpoint is {diff} degrees lower than your state\'s average.'.format(diff=diff)
        elif avg > stavg:
            diff = avg - stavg
            diffst = 'Your household setpoint is {diff} degrees higher than your state\'s average.'.format(diff=diff)
        else:
            diff = 0
            diffst = 'Your household setpoint is equal to your state\'s average.'
        result_dict = {
                    'user': 'Your average temperature is {user}.'.format(user=avg),
                    'region': 'Your region\'s average temperature is {regavg}.'.format(regavg=regavg),
                    'state': 'Your state\'s average temperature is {stavg}.'.format(stavg=stavg),
                    'diff': diffst}
        region_template = template_env.get_template('templates/region.html')
        self.response.write(region_template.render(result_dict))

class AppliancePage(webapp2.RequestHandler):
    def get(self):
        beg_template = template_env.get_template('templates/appliances.html')
        self.response.write(beg_template.render())

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        ac=self.request.get('ac-type')
        ac = int(ac)
        price = self.request.get('state')
        price = str(price)
        seer = seers(ac)
        size = sizes(ac)
        money = states(price)
        my_dict = {'seer': seer, 'sizes': size, 'money': money}
        end_template = template_env.get_template('templates/app-results.html')
        self.response.write(end_template.render(my_dict))

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/region', RegionPage),
    ('/appliances', AppliancePage),
], debug=True)
