import requests
import wikipedia

cmd= "https://en.wikipedia.org/w/api.php?action=query&format=json&list=categorymembers&cmtitle=Category%3AAll%20articles%20with%20peacock%20terms&cmcontinue=page%7C312f353103064f373104312f353104098c41293f29594d3929098e011c01dcc2dcc3dcc1dc0c%7C5177157&cmlimit=max"
text = requests.get(cmd).json()


tentative = set()
print(text)
for pagename in text['query']['categorymembers']:
    try:
        print(pagename)
        t = wikipedia.page(pagename['title'])
        raw = t.html().split('\n')[4:]
        for line in raw:
            if "peacock" in line:
                tentative.add(pagename['title'])
                print(pagename['title'])
    except:
        pass
print(tentative)

s = {'Warren Berger', 'Elizabeth Becker', 'Bibliotheca Alexandrina', 'Sylvia Bongo Ondimba', 'Susanne Boll', 'AusIndustry', 'Robert Boynes', 'Astra-Sesefsky', 'American Educational Research Association', 'Mai Atafo', 'Mazyar Asadi', 'Binding problem', 'Bucks County Playhouse', 'Shiv Dayal Batish', 'Patrick Alavi', 'AWTF-80 SC', 'B-Projekt', '82nd Training Wing', 'Arts-based training', 'Jaime Awe', 'S. M. Balaji', 'Mark Braverman', 'Simon Aldridge', 'Robert J. Bolger', 'Andrew Bird', 'Robert Allan Black', 'Bureau of International Information Programs', 'Bhavadhaarini', 'ASC San Diego', 'Svend Brinkmann', 'Larry Beinfest', '10 Days on the Island', 'Stuart Bowen', 'Arden-Arcade, California', '2016–17 Coupe de France Preliminary Rounds, Alsace, Lorraine and Champagne-Ardenne', 'Abhay and Rani Bang', 'Nariman Behravesh', 'British International School of Chicago Lincoln Park', 'Basti Islamabad', 'Carla L. Benson', 'James Bundy', 'Banff Sunshine', 'Belize Basketball Federation', 'Asbestos Records', '2018 Saint Francis Cougars football team', 'Mohammed Aziz', '2016–17 Coupe de France Preliminary Rounds, Picardie and Nord-Pas de Calais', 'Wael Arakji', 'Paul Barber (soccer administrator)', 'Beyoncé Pulse', 'ANU Press', 'Kevin Bales', 'Peeter All', 'Sam Byibesho', 'Nazir Ahmad (neurosurgeon)', 'Algoa Bay Yacht Club', 'Vivian Bales', 'Nirmal Prabha Bordoloi', 'Rym Breidy', 'Business activity monitoring', 'Bank Menatep', 'Beta Sigma Psi', 'Aanchol', 'Bioelectricity', 'Kimo Armitage', 'Bronzeville (play)', 'Healy Baumgardner', 'Chris Aire', 'Frank Beddor', 'Charles Billich', 'Balachaur', 'Belgian Warmblood', '2017 ICC Champions Trophy Final', 'Michael Attree', 'Miriam Beerman', 'John Butcher (Australian footballer)', 'Julie Bell', 'Andrew Blackman', 'Berlin School of Creative Leadership', 'Gruppo Bertone', 'A. R. Bernard', 'Belime', 'Battle of Marignano', 'Edward Burtynsky', 'Mónica Bertolino', 'Christian de Boisredon', 'Accordion', 'Albert Asriyan', 'Wellesley Bailey', 'Adamu Bello', 'Bouldin Creek, Austin, Texas', 'Bangomunda', '2013 Shahbag protests', 'William C. Burton', 'After School Club', 'Jaya Ahsan', 'Börse Berlin', 'AlphaSphere (instrument)', 'Richard Anuszkiewicz', 'Valda Berzins', 'Roger Boas', 'Bon Secours Wellness Arena', 'Takashi Amano', 'Octavius Black', 'Herman Basudde', 'Bread of Life Ministries International', 'Anton Belyaev', 'Alice Mamaga Akosua Amoako', 'S. S. Balan', 'Ellen S. Berscheid', 'Alberto Aquilani', 'Bunkered', 'Paul DH Baylay', '40th Airlift Squadron', 'Yogi Aaron', 'Alejandro Badia', 'Marilyn Beck', 'Carl Oscar Boije af Gennäs', 'Arcon 2', 'Academy of Nutrition and Dietetics', 'Nigel Benn', 'Sergio Bustamante (artist)', '2016–17 Coupe de France Preliminary Rounds', 'Ann Louise Bardach', 'Atom on Sphere', '3 Quarks Daily', 'Ambuthirtha', 'Abbotsleigh', 'Nahid Angha', 'Brandchannel', 'Rachel Attas', 'All India Students Federation', 'Jackson Anthony', 'Madhuri Banerjee', 'Mario Bellini', 'Dimitri Basilaia', 'Bentley R Type', 'Blasphemy law in the United Kingdom', 'Aquademics', 'Don Ahn', 'Oleg Bakhmatyuk', 'Khadgajeet Baral', 'Bobby Joe Ebola and the Children MacNuggits', 'Vyacheslav Artyomov', 'Neil Anderson (author)', 'Syeda Ummehani Ashraf', 'Born to Run (Bruce Springsteen song)', 'Les Baux-de-Provence', 'Azzedine Bousseksou', 'Ross Bailey', 'Birla Institute of Technology, Mesra', '18th Flight Test Squadron', 'Carlo Brandelli', 'Dave Burgering', 'British Nuclear Fuels Ltd', 'Baidu Tieba', 'Tom Barabas', 'Terry Burrus', 'Abiola Ajimobi', 'Janis Brenner', 'Abul Wafa Al Afghani', 'Prakash Yashwant Ambedkar', 'Aspirus Medford Hospital', 'Bankard', 'Wale Babalakin', 'Aberdeen floating village', 'Adas Israel Congregation (Washington, D.C.)', 'James Balog', 'Beehive Science and Technology Academy', '12th Airborne Command and Control Squadron', 'Mohammad Azharuddin', 'Deepak Bhojwani', 'Anything But Conservative', 'Brighton Collectibles', 'Saleem Ahmed', '136th Civil Engineer Squadron', 'Marco Angelini', 'Asymmetric warfare', 'Aspen Pharmacare', 'Bladensburg High School', 'Robert Boury', 'Karen Boustany', 'William Byrd II', 'All Things at Once', 'Steven Assael', 'Nnamdi Anyaehie', 'Kálmán Balogh', 'Acharyakulam', 'Atomic Energy Central School', 'Aussie Racing Cars', 'Apexart', 'Bohai University', 'Renée C. Byer', 'Bhaskaravarman', 'Pinky Anand', 'Baedeker', 'Aperture Entertainment', 'Shusmita Anis', 'CSS Acadia', 'Asia Pacific Week', 'Carolyne Barry', 'Svenska Bergsbruk', 'Stanford Blade', 'Arbovirus (band)', 'Marcus Baby', '2016 Pro Kabaddi League season (January)', 'Accident (1985 film)', 'Andhra Pradesh Residential Degree College', 'Benny Abante', 'Arthur Barnett Ltd', 'Mike Batt', 'Bilashati Tamiz Uddin High School', 'Omri Amrany', 'Alpha Nu Omega', 'Balgowlah Boys Campus', 'Battle of Palkhed', 'The Blue Generation', 'David Berg', 'Breite Oak Tree Reserve', 'Béla Bartók Music High School', 'Todd Bernstein', 'Dale Abenojar', 'Syed Baqar Askary', 'Derek Boshier', 'Anna Berndtson', 'Alpha Chi Omega', 'Atlas Mira', 'Elmira Bayrasli', 'Alhambra Theatre (Cape Town)', 'Aprilia', 'Tiana Alexandra', 'Application Defined Network', 'Mike Beedle', 'Blue Scholars', 'Nzinga Blake', 'Pierrick Boyer', 'David Burris', 'Alpha Phi', 'Ashish Bhasin', '2016 WNBA Finals', 'Kailash Bhansali', 'Al-Andalus', 'Sebastián Arce', 'Nurhan Atasoy', 'Barnes Wallis Academy', 'Bodybuilders (On the Inside)', 'Babhangawan', 'AZ Business Magazine', 'Paulo Branco', 'Baku White City', 'Yogeshwar Amatya', 'Gregorio Baro', 'Brockington College', 'Alpha Kappa Delta', 'Ravindra Amonkar', 'Ian Birkby', '133rd Engineer Battalion', 'AHDB Potatoes', 'Bakshaish', 'Bor Skate Plaza', 'Khodr Alama', 'Alliance Academy International', 'Seb Bishop', 'Januarius Jingwa Asongu', 'Lise Bach Hansen', 'Arm wrestling', 'Tarek Ben Halim', 'Architecture of Kerala', 'Donald Attig', 'Lave Knud Broch', 'Baylor University Chamber of Commerce', '5th Expeditionary Space Operations Squadron', 'Bihari culture', 'Jeremy Bates (boxer)', 'Arab American University (Palestine)', 'Abdulkarim Zanjani', 'Phaedon Avouris', 'Advaxis', 'Joseph Beer', 'Elena Barmakova', 'Bytown Boys Supporters Club', 'Fuad Akhundov', 'Dmitriy Aksyonov', 'Jenni Alpert', 'William S. Ballenger Sr.', 'Karen Asatrian', 'Peter Bazalgette', 'Bhadran (director)', 'Blackout Day', 'Kopil Bora', 'Nick Allbrook', 'Anas Aremeyaw Anas', '369th Croatian Reinforced Infantry Regiment (Wehrmacht)', 'Anselm Adodo', 'Mahavatar Babaji', 'Ash Adams', 'Bazaruto Archipelago National Park', 'Armin Pumpanmuang', 'Anita Altman', 'Solomon Adun Asemota', 'Miguel Ángel Biazzi', 'Business–IT alignment', 'The Art of Living International Center', 'Monika Bulanda', 'Bendigo Easter Festival', 'Samir Bağırov', 'Gary Bennett (politician)', 'Evan Peter Aurand', 'Toby Anstis', 'Jewel Aich', 'Bay to Bay yacht race', 'Michael Bywater', 'Austin FX4',
'Casalini', 'Imran Channa', 'Alex Campbell (singer)', 'Deepan Chakravarthy', 'Mauro Cappelletti', 'Ciudad de las Ideas (conference)', 'Dubai Smart Police Stations', 'Clean Air India Movement', 'Sylvia Convey', 'Cambridge Christian School (Tampa, Florida)', 'Dunya School', 'Michael Drobot', 'Carnegie Institution for Science', 'Concept-driven strategy', 'Chang Ping', 'Columbia University Partnership for International Development', 'Design Patterns', 'Jean-Pierre Dutilleux', 'Center of Gravity (festival)', 'Eastern Technical High School', 'Howard Davis (chemical engineer)', 'Candocuronium iodide', 'Chase Atlantic', 'Crossbar latch', 'Dhananjayans', 'Cul-de-sac (play)', 'Digital twin', 'De Havilland Canada Dash 8', 'Duck decoy (model)', 'Chrysalis High', 'Caruso St John', 'Chokher Bali (film)', 'Holly Carter', 'Andrew Cook (businessman)', 'Matt Cimber', 'Culture of Dhaka', 'Pierre El Daher', 'Dunbrody Country House Hotel', 'Paul Dujardin (art historian)', 'Chandler, Arizona', 'Will Durant', 'Astrid Chevallier', 'Eden Electronics', 'Cryptic Fate', 'Camp Marmal', 'Cepheid Inc', 'Childcare voucher scheme', 'Codementor', 'Giulio Dilemmi', 'Doug Cooper (author)', 'Gary Day (musician)', 'Diagnostic Enterprise Method', 'Kaushiki Chakraborty', 'Dan Reed Network', 'DePaul University', 'Grat Dalton', 'Economy of Vietnam', 'Swapan Chattopadhyay', 'Diversionary foreign policy', 'Jacques Cohen', 'Mahesh Desai', 'Sarah Daniels', 'Srinwanti Chakrabarti', 'Samaya Clark-Gabriel', 'Culture of the Southern United States', 'The Colony High School', 'Pollyanna Chu', "Dino and Carlo's Bar", 'Jim Castillo', 'Karen Joubert Cordier', 'Directorate-General for Communications Networks, Content and Technology', 'CalTV', 'Constantinos Charalambidis', 'Culture in Prizren', 'The ClueFinders', 'Aminuddin Dagar', 'Economy of Indonesia', 'Donna Robinson Divine', 'Culture of Texas', 'Ashley Coleman', 'Council for Affordable Quality Healthcare', 'Cluster of Excellence "Asia and Europe in a Global Context"', 'George A. David', 'Pankaj Dubey', 'Anja Dittmer', 'Bimbo Daramola', 'Canadian Armed Forces Divers', 'Delta Delta Delta', 'EDAPS', 'Cross Rhythms', 'Diocese of Dornakal of the Church of South India', 'Prem Ram Dubey', 'Soumitra Dutta', 'Fred J. Eckert', 'Cyril Desbruslais', 'Chen Yifei', 'Cathy Davis', 'Michele Cassou', 'David Downton', 'EAOP', 'Chuckmuck', 'Hugo de Burgh', 'Shekhar Dixit', 'Digital Advertising Alliance of Canada', 'CGMP-specific phosphodiesterase type 5', 'Joe DeNardo', 'National Center for Civil and Human Rights', 'Dilkon, Arizona', "Cam'ron", 'Civil Aviation High School, Tejgaon', "Nicola D'Onofrio", 'Anthony Crivello', 'Darashaw', 'Cameron Colvin', 'K. C. Das', 'Dewey Defeats Truman (band)', 'The Colorado Health Foundation', 'Jeffrey Collé', 'Shelly Crane', 'Roberto Duailibi', 'Classic 263', 'Den-en-chōfu', 'Congressional Award', 'Christian Business Faculty Association', 'Nils Daulaire', 'Camper (company)', 'Commando Battalion for Resolute Action', 'Jim Connors', 'Dublin Wives', 'Croatian nobility', 'Danny Diablo', 'Campaigns & Communications Group', 'Dr. S. Hussain Zaheer Memorial High School', 'Child of the Sun', 'Edniesha Curry', 'Dhantoli', 'Steve DeAngelo', 'Digital Bros', 'Dell Studio', 'List of Disney Channel series', 'Dhol Somudur', 'CCFilms', 'Bridget Carragher', 'Kelvin Chan', 'Colonial Brazil', 'COVID-19 pandemic in Sweden', 'Alassane Diago', 'Mark Casson', 'Carlo Catassi', 'Amlan Datta', 'Mike Dred', 'Cult brand', 'Chief diversity officer', 'Colombo City Centre', 'The East Is Red (1965 film)', 'Mark Dennis (director)', 'Cole Classic', 'Circular procurement', 'Rasbihari Desai', 'East Africa rugby union team', 'Lloyd Daniels', 'Caliber Home Loans', 'Doping in East Germany', 'Piotr Damasiewicz', 'Cidinho and Doca', 'Pete Cooke', 'CoolSPICE', 'EastWest Bank', 'Customer success', 'Dental spa', 'Aeneas Coffey', 'Billy Dec', 'Roger Counsil', 'Ron Cahute', 'Jimmy Case', 'Susane Colasanti', 'Gordon Cheung', 'Cone calorimeter', 'California State Route 123', 'Eatliz', 'Campbell Collegiate', 'Customer relationship management', 'Continuity (fiction)', 'Samier Dandan', 'Dumka', 'Jon Robert Cart', 'Juan Manuel De la Rosa', 'Delhi Public School Aligarh', 'De La Salle Supervised Schools', 'Michael A. Costello', 'Silvio Denz', 'Carlos Coste', 'Dror-Israel', 'Chessington World of Adventures', 'John C. Corlette', 'Richa Chadda', 'Council for World Mission', 'Guy Eckstine', 'Sal Cuevas', 'Oksana Chusovitina', 'Adam Edelen', 'María Leoba Castañeda Rivas', 'Raymond J. Chambers', 'Defense Equal Opportunity Management Institute', 'Destination club'}
