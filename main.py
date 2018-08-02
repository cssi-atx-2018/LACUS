import webapp2
import jinja2
import air_con

template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env=jinja2.Environment(loader=template_loader)

"""ac_dict = {"Trane XV20i TruComfort Variable Speed, Model 4TTV0024A": [22, 24000],
    "Trane XV20i TruComfort Variable Speed, Model 4TTV0036A": [22, 36000],
    "Trane XV20i TruComfort Variable Speed, Model 4TTV0048A": [22, 48000],
    "Trane XV20i TruComfort Variable Speed, Model 4TTV0060A": [22, 60000]}
states_dict = {'Texas': 10.98}"""

def avgthese(a, b):
    one = int(a)
    two = int(b)
    sum = one+two
    return sum/2

class HomePage(webapp2.RequestHandler):
    def get(self):
        home_temp = template_env.get_template('templates/home.html')
        self.response.write(home_temp.render())

class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_temp = template_env.get_template('templates/about.html')
        self.response.write(about_temp.render())

class RegionPage(webapp2.RequestHandler):
    def get(self):
        region_template = template_env.get_template('templates/region.html')
        self.response.write(region_template.render())

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        region = self.request.get('region')
        state = self.request.get('state')
        min = self.request.get('mintemp')
        max = self.request.get('maxtemp')
        avg = avgthese(min, max)
        regavg = {'NorthEast': 64.37, 'MidWest': 67.6, 'South': 69.16}
        neavg = {'Maine': 65.5, 'New Hampshire': 64.2, 'Vermont': 63.4}
        mwavg = {'Iowa': 65.5, 'Nebraska': 69.7}
        savg = {'Delaware': 66.3, 'Mississippi': 69.8, 'Louisiana': 69.8, 'Oklahoma': 70, 'Texas': 69.9}
        if region == 'NorthEast':
            region_avg = regavg['NorthEast']
            if state == 'Maine':
                state_avg = neavg['Maine']
            elif state == 'New Hampshire':
                state_avg = neavg['New Hampshire']
            elif state == 'Vermont':
                state_avg = neavg['Vermont']
        elif region == 'MidWest':
            region_avg = regavg['MidWest']
            if state == 'Iowa':
                state_avg = mwavg['Iowa']
            elif state == 'Nebraska':
                state_avg = mwavg['Nebraska']
        elif region == 'South':
            region_avg = regavg['South']
            if state == 'Delaware':
                state_avg = savg['Delaware']
            elif state == 'Mississippi':
                state_avg = savg['Mississippi']
            elif state == 'Louisiana':
                state_avg = savg['Louisiana']
            elif state == 'Oklahoma':
                state_avg = savg['Oklahoma']
            elif state == 'Texas':
                state_avg = savg['Texas']

        if avg < state_avg:
            diff = state_avg - avg
            diffst = 'Your household setpoint is {diff} degrees lower than your state\'s average.'.format(diff=diff)
        elif avg > state_avg:
            diff = avg - state_avg
            diffst = 'Your household setpoint is {diff} degrees higher than your state\'s average.'.format(diff=diff)
        else:
            diff = 0
            diffst = 'Your household setpoint is equal to your state\'s average.'
        result_dict = {
                    'user': 'Your average temperature is {user}.'.format(user=avg),
                    'region': 'Your region\'s average temperature is {regavg}.'.format(regavg=region_avg),
                    'state': 'Your state\'s average temperature is {stavg}.'.format(stavg=state_avg),
                    'diff': diffst}
        region_template = template_env.get_template('templates/region.html')
        self.response.write(region_template.render(result_dict))

class AppliancePage(webapp2.RequestHandler):
    def get(self):
        beg_template = template_env.get_template('templates/app-results.html')
        ac_arr=[]
        states_arr=[]
        for pair in sorted(air_con.ac_dict.items()):
            ac_arr.append(pair[0])
        for pair in sorted(air_con.states_dict.items()):
            states_arr.append(pair[0])
        dict = {'dict': ac_arr, 's_dict': states_arr, 'my_dict':{}}
        self.response.write(beg_template.render(dict))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        ac=str(self.request.get('ac-type'))
        ac2=str(self.request.get('ac-type-2'))
        state = str(self.request.get('state'))
        state2 = str(self.request.get('state-2'))
        ac_arr=[]
        states_arr=[]
        for pair in sorted(air_con.ac_dict.items()):
            ac_arr.append(pair[0])
        for pair in sorted(air_con.states_dict.items()):
            states_arr.append(pair[0])
        dict = {'dict': ac_arr, 's_dict': states_arr}
        seer = air_con.ac_dict[ac][0]
        size = air_con.ac_dict[ac][1]
        seer2 = air_con.ac_dict[ac2][0]
        size2 = air_con.ac_dict[ac2][1]
        money = air_con.states_dict[state]
        money2 = air_con.states_dict[state2]
        my_dict = {'dict': ac_arr, 's_dict': states_arr, 'my_dict':{'name1': ac, 'name2': ac2, 'state': state, 'seer': seer, 'size': size, 'money': money, 'money2': money2, 'seer2': seer2, 'size2': size2, 'state2': state2}}
        end_template = template_env.get_template('templates/app-results.html')
        self.response.write(end_template.render(my_dict))

class SolutionsPage(webapp2.RequestHandler):
    def get(self):
        sol_temp = template_env.get_template('templates/solutions.html')
        self.response.write(sol_temp.render())

class MapPage(webapp2.RequestHandler):
    def get(self):
        map_temp = template_env.get_template('templates/map.html')
        self.response.write(map_temp.render())

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/map', MapPage),
    ('/about', AboutPage),
    ('/region', RegionPage),
    ('/appliances', AppliancePage),
    ('/solutions', SolutionsPage),
], debug=True)
