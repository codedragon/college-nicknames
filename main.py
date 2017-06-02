#!/usr/local/bin/python3
"""College Nicknames Alexa Skill

This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
import math
import random
import string


# ------- Skill specific business logic -------
GAME_LENGTH = 5
SKILL_NAME = "College Nicknames"

# When editing your questions pay attention to your punctuation.
# Make sure you use question marks or periods.
# Make sure the first answer is the correct one.

# If there are multiple valid answers, provide all of them in the answers array.
#   {"Name an element with 8 valence electrons.": ["Neon", "Argon", "Krypton", "Xenon", "Radon"]},
#QUESTIONS = [
#    {"What is the nickname for University of Washington?": ["Huskies"]},
#    {"What is the nickname for Abilene Christian University?": ["Wildcats"]},
#    {"What is the nickname for Adams State?": ["Grizzlies"]},
#    {"What is the nickname for Adelphi": ["Panthers"]},
#    {"What is the nickname for Adrian College?": ["Bulldogs"]},
#    {"What is the nickname for Air Force?": ["Falcons"]},
#]

QUESTIONS = [
    {"What is the nickname for Abilene Christian University?": ["Wildcats"]},
    {"What is the nickname for Adams State?": ["Grizzly Bear", "Grizzlies"]},
    {"What is the nickname for Adelphi?": ["Cougar", "Panthers"]},
    {"What is the nickname for Adrian College?": ["Bulldogs"]},
    {"What is the nickname for Air Force?": ["Falcons"]},
    {"What is the nickname for Akron?": ["Zips"]},
    {"What is the nickname for Alabama Crimson?": ["Tide"]},
    {"What is the nickname for Alabama-Birmingham?": ["Blazers"]},
    {"What is the nickname for Alabama-Huntsville?": ["Chargers"]},
    {"What is the nickname for Alabama A and M?": ["Bulldogs", "Lady Bulldogs"]},
    {"What is the nickname for Alabama State?": ["Hornets", "Lady Hornets"]},
    {"What is the nickname for Alaska Anchorage?": ["Seawolves"]},
    {"What is the nickname for Alaska Fairbanks?": ["Nanooks"]},
    {"What is the nickname for Albany?": ["Great Danes"]},
    {"What is the nickname for Albright College?": ["Lions"]},
    {"What is the nickname for Alcorn State?": ["Braves", "Lady Braves"]},
    {"What is the nickname for Albertus Magnus College?": ["Falcons"]},
    {"What is the nickname for Alderson-Broaddus College?": ["Battlers"]},
    {"What is the nickname for Alfred University?": ["Saxons"]},
    {"What is the nickname for Alice Lloyd College?": ["Eagles"]},
    {"What is the nickname for Alvernia University?": ["Crusaders"]},
    {"What is the nickname for American International College?": ["Yellowjackets"]},
    {"What is the nickname for American University?": ["Eagles"]},
    {"What is the nickname for Amherst College?": ["Lord Jeffs"]},
    {"What is the nickname for Anderson University, Indiana?": ["Ravens"]},
    {"What is the nickname for Anderson University, South Carolina?": ["Trojans"]},
    {"What is the nickname for Angelo State University?": ["Rams Rambelles", "'Belles"]},
    {"What is the nickname for Appalachian State University?": ["Mountaineers"]},
    {"What is the nickname for Arcadia University?": ["Knights"]},
    {"What is the nickname for Arizona?": ["Wildcats"]},
    {"What is the nickname for Arizona State University?": ["Sun Devils"]},
    {"What is the nickname for Arkansas?": ["Razorbacks"]},
    {"What is the nickname for Arkansas-Little Rock?": ["Trojans"]},
    {"What is the nickname for Arkansas-Monticello?": ["Boll Weevils", "Cotton Blossoms"]},
    {"What is the nickname for Arkansas-Pine Bluff?": ["Golden Lions"]},
    {"What is the nickname for Arkansas State University?": ["Red Wolves"]},
    {"What is the nickname for Arkansas Tech University?": ["Wonder Boys", "Golden Suns"]},
    {"What is the nickname for Army?": ["Black Knights"]},
    {"What is the nickname for ASA College, Miami?": ["Silver Storm"]},
    {"What is the nickname for ASA College, New York?": ["Avengers"]},
    {"What is the nickname for Ashford University?": ["Saints"]},
    {"What is the nickname for Ashland University?": ["Eagles"]},
    {"What is the nickname for Association Free Lutheran Bible School and Seminary?": ["Conquerors"]},
    {"What is the nickname for Assumption College?": ["Greyhounds"]},
    {"What is the nickname for Auburn University?": ["Tigers", "Plainsmen"]},
    {"What is the nickname for Auburn University at Montgomery?": ["Senators"]},
    {"What is the nickname for Augsburg College?": ["Auggies"]},
    {"What is the nickname for Augustana College?": ["Vikings"]},
    {"What is the nickname for Aurora University?": ["Spartans"]},
    {"What is the nickname for Austin College?": ["Kangaroos"]},
    {"What is the nickname for Austin Peay State University?": ["Governors", "Lady Govs"]},
    {"What is the nickname for Ave Maria University?": ["Gyrenes"]},
    {"What is the nickname for Avila University?": ["Eagles"]},
    {"What is the nickname for Azusa Pacific University?": ["Cougars"]},
    {"What is the nickname for Babson College?": ["Beavers"]},
    {"What is the nickname for Baker University?": ["Wildcats"]},
    {"What is the nickname for Baldwin-Wallace College?": ["Yellow Jackets"]},
    {"What is the nickname for Ball State University?": ["Cardinals"]},
    {"What is the nickname for Bard College?": ["Raptors"]},
    {"What is the nickname for Barry University?": ["Buccaneers"]},
    {"What is the nickname for Bates College?": ["Bobcats"]},
    {"What is the nickname for Baylor University?": ["Bears", "Lady Bears"]},
    {"What is the nickname for Bellevue University?": ["Bruins"]},
    {"What is the nickname for Belmont University?": ["Bruins"]},
    {"What is the nickname for Belmont Abbey College?": ["Crusaders"]},
    {"What is the nickname for Beloit College?": ["Buccaneers"]},
    {"What is the nickname for Bemidji State University?": ["Beavers"]},
    {"What is the nickname for Benedict College?": ["Tigers"]},
    {"What is the nickname for Benedictine College?": ["Ravens"]},
    {"What is the nickname for Bentley College?": ["Falcons"]},
    {"What is the nickname for Berea College?": ["Mountaineers"]},
    {"What is the nickname for Bethany College, Kansas?": ["Swedes"]},
    {"What is the nickname for Bethany College, West Virginia?": ["Bison"]},
    {"What is the nickname for Bethel College, Indiana?": ["Pilots"]},
    {"What is the nickname for Bethel College, Kansas?": ["Threshers"]},
    {"What is the nickname for Bethel University, Minnesota?": ["Royals"]},
    {"What is the nickname for Bethel University, Tennessee?": ["Wildcats"]},
    {"What is the nickname for Bethune-Cookman College?": ["Wildcats"]},
    {"What is the nickname for Binghamton University?": ["Bearcats"]},
    {"What is the nickname for Birmingham-Southern College?": ["Panthers"]},
    {"What is the nickname for Black Hills State University?": ["Yellow Jackets"]},
    {"What is the nickname for Blinn College?": ["Buccaneers"]},
    {"What is the nickname for Bloomfield College?": ["Deacons"]},
    {"What is the nickname for Bloomsburg University?": ["Huskies"]},
    {"What is the nickname for Bluefield College?": ["Rams"]},
    {"What is the nickname for Bluefield State College?": ["Big Blues", "Lady Blues"]},
    {"What is the nickname for Bluffton University?": ["Beavers"]},
    {"What is the nickname for Boise State University?": ["Broncos"]},
    {"What is the nickname for Boston College?": ["Eagles"]},
    {"What is the nickname for Boston University?": ["Terriers"]},
    {"What is the nickname for Bowling Green State University?": ["Falcons"]},
    {"What is the nickname for Bowdoin College?": ["Polar Bears"]},
    {"What is the nickname for Bowie State University?": ["Bulldogs"]},
    {"What is the nickname for Bradley University?": ["Braves"]},
    {"What is the nickname for Brandeis University?": ["Judges"]},
    {"What is the nickname for Briarcliffe College?": ["Seahawks"]},
    {"What is the nickname for Brigham Young University?": ["Cougars"]},
    {"What is the nickname for Brigham Young University, Hawaii?": ["Seasiders"]},
    {"What is the nickname for Bryant University?": ["Bulldogs"]},
    {"What is the nickname for Brooklyn College?": ["Bulldogs"]},
    {"What is the nickname for Broward College?": ["Seahawks"]},
    {"What is the nickname for Brown University?": ["Bears"]},
    {"What is the nickname for Bucknell University?": ["Bison"]},
    {"What is the nickname for Buena Vista University?": ["Beavers"]},
    {"What is the nickname for Buffalo?": ["Bulls"]},
    {"What is the nickname for Buffalo State College?": ["Bengals"]},
    {"What is the nickname for Butler University?": ["Bulldogs"]},
    {"What is the nickname for Cabrini College?": ["Cavaliers"]},
    {"What is the nickname for University of California, Berkeley?": ["Golden Bears"]},
    {"What is the nickname for University of California, Davis?": ["Aggies"]},
    {"What is the nickname for University of California, Irvine?": ["Anteaters"]},
    {"What is the nickname for University of California, Merced?": ["Golden Bobcats"]},
    {"What is the nickname for University of California, Riverside?": ["Highlanders"]},
    {"What is the nickname for University of California, San Diego?": ["Tritons"]},
    {"What is the nickname for University of California, Santa Barbara?": ["Gauchos"]},
    {"What is the nickname for University of California, Santa Cruz?": ["Banana Slugs"]},
    {"What is the nickname for University of California, Los Angeles?": ["Bruins"]},
    {"What is the nickname for California Lutheran University?": ["Kingsmen", "Regals"]},
    {"What is the nickname for California Maritime Academy?": ["Keelhaulers"]},
    {"What is the nickname for California State Polytechnic University, Pomona?": ["Broncos"]},
    {"What is the nickname for California Polytechnic State University San Luis Obispo?": ["Mustangs"]},
    {"What is the nickname for California State University, Bakersfield?": ["Roadrunners"]},
    {"What is the nickname for California State University, Channel Islands?": ["Dolphins"]},
    {"What is the nickname for California State University, Chico?": ["Wildcats"]},
    {"What is the nickname for California State University, East Bay?": ["Pioneers"]},
    {"What is the nickname for California State University, Fresno?": ["Bulldogs"]},
    {"What is the nickname for California State University, Fullerton?": ["Titans"]},
    {"What is the nickname for California State University, Humboldt?": ["Jacks"]},
    {"What is the nickname for California State University, Long Beach?": ["49ers"]},
    {"What is the nickname for California State University, Los Angeles?": ["Golden Eagles"]},
    {"What is the nickname for California State University, Northridge?": ["Matadors"]},
    {"What is the nickname for California State University, San Bernardino?": ["Coyotes"]},
    {"What is the nickname for California State University, San Diego?": ["Aztecs"]},
    {"What is the nickname for California State University, San Francisco?": ["Gators"]},
    {"What is the nickname for California State University, San Jose?": ["Spartans"]},
    {"What is the nickname for California State University, Sacramento?": ["Hornets"]},
    {"What is the nickname for California State University, Sonoma?": ["Seawolves"]},
    {"What is the nickname for California State University, Stanislaus?": ["Warriors"]},
    {"What is the nickname for California University of Pennsylvania?": ["Vulcans"]},
    {"What is the nickname for Calvin College?": ["Knights", "Lady Knights"]},
    {"What is the nickname for Campbell University?": ["Fighting Camels"]},
    {"What is the nickname for Campbellsville University?": ["Tigers"]},
    {"What is the nickname for Canisius College?": ["Golden Griffins"]},
    {"What is the nickname for Cankdeska Cikana Community College?": ["C4"]},
    {"What is the nickname for Capital University?": ["Crusaders"]},
    {"What is the nickname for Cardinal Stritch University?": ["Wolves"]},
    {"What is the nickname for Carleton College?": ["Knights"]},
    {"What is the nickname for Carnegie Mellon University?": ["Tartans"]},
    {"What is the nickname for Carson-Newman College?": ["Eagles"]},
    {"What is the nickname for Carthage College?": ["Red Men", "Lady Reds"]},
    {"What is the nickname for Case Western Reserve University?": ["Spartans"]},
    {"What is the nickname for Castleton State College?": ["Spartans"]},
    {"What is the nickname for The Catholic University of America?": ["Cardinals"]},
    {"What is the nickname for Cazenovia College?": ["Wildcats"]},
    {"What is the nickname for Centenary College?": ["Gentlemen", "Ladies"]},
    {"What is the nickname for Central Arkansas?": ["Bears", "Sugar Bears"]},
    {"What is the nickname for Central Connecticut State University?": ["Blue Devils"]},
    {"What is the nickname for College of Central Florida?": ["Patriots"]},
    {"What is the nickname for Central Florida?": ["Knights"]},
    {"What is the nickname for Central College, Iowa?": ["Dutch"]},
    {"What is the nickname for Central Methodist University?": ["Eagles"]},
    {"What is the nickname for Central Michigan University?": ["Chippewas"]},
    {"What is the nickname for Central Missouri?": ["Mules", "Jennies"]},
    {"What is the nickname for Central Oklahoma University?": ["Bronchos"]},
    {"What is the nickname for Central Washington University?": ["Wildcats"]},
    {"What is the nickname for Centre College?": ["Colonels"]},
    {"What is the nickname for Cerritos College?": ["Falcons"]},
    {"What is the nickname for Chadron State College?": ["Eagles"]},
    {"What is the nickname for Chaminade University?": ["Silverswords"]},
    {"What is the nickname for Chapman University?": ["Panthers"]},
    {"What is the nickname for College of Charleston?": ["Cougars"]},
    {"What is the nickname for Chatham University?": ["Cougars"]},
    {"What is the nickname for University of Charleston, West Virginia?": ["Golden Eagles"]},
    {"What is the nickname for Charleston Southern University?": ["Buccaneers", "Lady Bucs"]},
    {"What is the nickname for Chestnut Hill College?": ["Griffins"]},
    {"What is the nickname for Cheyney University?": ["Wolves"]},
    {"What is the nickname for Chicago?": ["Maroons"]},
    {"What is the nickname for Chicago State University?": ["Cougars"]},
    {"What is the nickname for Chipola College?": ["Indians"]},
    {"What is the nickname for Christian Brothers University?": ["Buccaneers"]},
    {"What is the nickname for Christopher Newport University?": ["Captains"]},
    {"What is the nickname for Cincinnati?": ["Bearcats"]},
    {"What is the nickname for Cincinnati Christian University?": ["Eagles"]},
    {"What is the nickname for The Citadel?": ["Bulldogs"]},
    {"What is the nickname for Claremont McKenna College?": ["Stags", "Athenas"]},
    {"What is the nickname for Harvey Mudd College?": ["Stags", "Athenas"]},
    {"What is the nickname for Scripps College?": ["Stags", "Athenas"]},
    {"What is the nickname for Clarion University?": ["Golden Eagles"]},
    {"What is the nickname for Clarkson University?": ["Golden Knights"]},
    {"What is the nickname for Clarke University?": ["Crusaders"]},
    {"What is the nickname for Clearwater Christian College?": ["Cougars"]},
    {"What is the nickname for Clemson University?": ["Tigers"]},
    {"What is the nickname for Cleveland State University?": ["Vikings"]},
    {"What is the nickname for Coastal Carolina University?": ["Chanticleers", "Lady Chants"]},
    {"What is the nickname for Coe College?": ["Kohawks"]},
    {"What is the nickname for Coker College?": ["Cobras"]},
    {"What is the nickname for Colby College?": ["White Mules"]},
    {"What is the nickname for Colgate University?": ["Raiders"]},
    {"What is the nickname for Colorado?": ["Buffaloes"]},
    {"What is the nickname for Colorado-Colorado Springs?": ["Mountain Lions"]},
    {"What is the nickname for Colorado College?": ["Tigers"]},
    {"What is the nickname for Colorado Mesa University?": ["Mavericks", "Lady Mavs"]},
    {"What is the nickname for Colorado School of Mines?": ["Ore Diggers"]},
    {"What is the nickname for Colorado State University?": ["Rams"]},
    {"What is the nickname for Colorado State University-Pueblo?": ["ThunderWolves"]},
    {"What is the nickname for Columbia College, Missouri?": ["Cougars"]},
    {"What is the nickname for Columbia University?": ["Lions"]},
    {"What is the nickname for Concord University?": ["Mountain Lions", "Lady Lions"]},
    {"What is the nickname for Concordia College, Moorhead?": ["Cobbers"]},
    {"What is the nickname for Concordia College, Selma?": ["Hornets"]},
    {"What is the nickname for Concordia College, New York?": ["Clippers"]},
    {"What is the nickname for Concordia University, Ann Arbor?": ["Cardinals"]},
    {"What is the nickname for Concordia University Chicago?": ["Cougars"]},
    {"What is the nickname for Concordia University, Irvine?": ["Eagles"]},
    {"What is the nickname for Concordia University, Nebraska?": ["Bulldogs"]},
    {"What is the nickname for Concordia University, Portland?": ["Cavaliers"]},
    {"What is the nickname for Concordia University, Saint Paul?": ["Golden Bears"]},
    {"What is the nickname for Concordia University Texas?": ["Tornadoes"]},
    {"What is the nickname for Concordia University Wisconsin?": ["Falcons"]},
    {"What is the nickname for Connecticut?": ["Huskies"]},
    {"What is the nickname for Connecticut College?": ["Camels"]},
    {"What is the nickname for Coppin State University?": ["Eagles"]},
    {"What is the nickname for Cornell University?": ["Big Red"]},
    {"What is the nickname for Cornerstone University?": ["Golden Eagles"]},
    {"What is the nickname for Creighton University?": ["Blue Jays"]},
    {"What is the nickname for Culver-Stockton College?": ["Wildcats"]},
    {"What is the nickname for Cumberland University?": ["Phoenix"]},
    {"What is the nickname for Cumberlands?": ["Patriots"]},
    {"What is the nickname for Dallas Baptist University?": ["Patriots"]},
    {"What is the nickname for Dakota State University?": ["Trojans"]},
    {"What is the nickname for Dana College?": ["Vikings"]},
    {"What is the nickname for Dartmouth College?": ["Big Green"]},
    {"What is the nickname for Davis and Elkins College?": ["Senators"]},
    {"What is the nickname for Davenport University?": ["Panthers"]},
    {"What is the nickname for Davidson College?": ["Wildcats"]},
    {"What is the nickname for Dayton?": ["Flyers"]},
    {"What is the nickname for Daytona State College?": ["Falcons"]},
    {"What is the nickname for Defiance College?": ["Yellow Jackets"]},
    {"What is the nickname for DePaul University?": ["Blue Demons"]},
    {"What is the nickname for DePauw University?": ["Tigers"]},
    {"What is the nickname for Delaware?": ["Fightin' Blue Hens"]},
    {"What is the nickname for Delaware State University?": ["Hornets"]},
    {"What is the nickname for Delaware Valley College?": ["Aggies"]},
    {"What is the nickname for Delta State University?": ["Statesmen", "Lady Statesmen"]},
    {"What is the nickname for Denison University?": ["Big Red"]},
    {"What is the nickname for Denver?": ["Pioneers"]},
    {"What is the nickname for DeSales University?": ["Bulldogs"]},
    {"What is the nickname for Detroit?": ["Titans"]},
    {"What is the nickname for Dickinson College?": ["Red Devils"]},
    {"What is the nickname for District of Columbia?": ["Firebirds", "Lady Firebirds"]},
    {"What is the nickname for Doane College?": ["Tigers"]},
    {"What is the nickname for Dordt College?": ["Defenders"]},
    {"What is the nickname for Dowling College?": ["Golden Lions"]},
    {"What is the nickname for Drake University?": ["Bulldogs"]},
    {"What is the nickname for Drew University?": ["Rangers"]},
    {"What is the nickname for Drexel University?": ["Dragons"]},
    {"What is the nickname for Duke University?": ["Blue Devils"]},
    {"What is the nickname for Duquesne University?": ["Dukes"]},
    {"What is the nickname for Dubuque?": ["Spartans"]},
    {"What is the nickname for Earlham College?": ["Hustlin' Quakers"]},
    {"What is the nickname for Eastern Arizona College?": ["Gila Monsters"]},
    {"What is the nickname for East Carolina University?": ["Pirates"]},
    {"What is the nickname for East Los Angeles College?": ["Huskies", "Lady Huskies"]},
    {"What is the nickname for East Stroudsburg University?": ["Warriors"]},
    {"What is the nickname for East Tennessee State University?": ["Buccaneers", "Lady Bucs"]},
    {"What is the nickname for East Texas Baptist University?": ["Tigers"]},
    {"What is the nickname for Eastern Connecticut State University?": ["Warriors"]},
    {"What is the nickname for Eastern Florida State College?": ["Titans"]},
    {"What is the nickname for Eastern Illinois University?": ["Fighting Panthers"]},
    {"What is the nickname for Eastern Kentucky University?": ["Colonels", "Lady Colonels"]},
    {"What is the nickname for Eastern Michigan University?": ["Eagles"]},
    {"What is the nickname for Eastern Nazarene College?": ["Lions"]},
    {"What is the nickname for Eastern New Mexico University?": ["Greyhounds", "Zias"]},
    {"What is the nickname for Eastern University?": ["Eagles"]},
    {"What is the nickname for Eastern Washington University?": ["Eagles"]},
    {"What is the nickname for Eckerd College?": ["Tritons"]},
    {"What is the nickname for Edinboro University?": ["Fighting Scots"]},
    {"What is the nickname for Edward Waters College?": ["Tigers"]},
    {"What is the nickname for El Paso Community College?": ["Tejanos", "Lady Tejanos"]},
    {"What is the nickname for Elon University?": ["Phoenix"]},
    {"What is the nickname for Embry-Riddle Aeronautical University?": ["Eagles"]},
    {"What is the nickname for Emory University?": ["Eagles"]},
    {"What is the nickname for Emporia State University?": ["Hornets"]},
    {"What is the nickname for Endicott College?": ["Gulls"]},
    {"What is the nickname for Erskine College?": ["Flying Fleet"]},
    {"What is the nickname for Evangel University?": ["Crusaders"]},
    {"What is the nickname for Evansville?": ["Purple Aces"]},
    {"What is the nickname for Evergreen State College?": ["Geoducks"]},
    {"What is the nickname for Fairleigh Dickinson University, Florham Campus?": ["Devils"]},
    {"What is the nickname for Fairleigh Dickinson University, Metropolitan Campus?": ["Knights"]},
    {"What is the nickname for Fairfield University?": ["Stags"]},
    {"What is the nickname for Fairmont State University?": ["Falcons"]},
    {"What is the nickname for Faulkner University?": ["Eagles"]},
    {"What is the nickname for Ferris State University?": ["Bulldogs"]},
    {"What is the nickname for Felician College?": ["Golden Falcons"]},
    {"What is the nickname for Finlandia University?": ["Lions"]},
    {"What is the nickname for Fisk University?": ["Bulldogs"]},
    {"What is the nickname for Fitchburg State?": ["Falcons"]},
    {"What is the nickname for Flagler College?": ["Saints"]},
    {"What is the nickname for Florida?": ["Gators"]},
    {"What is the nickname for Florida A and M University?": ["Rattlers"]},
    {"What is the nickname for Florida Atlantic University?": ["Owls"]},
    {"What is the nickname for Florida International University?": ["Golden Panthers"]},
    {"What is the nickname for Florida College?": ["Falcons"]},
    {"What is the nickname for Florida Institute of Technology?": ["Panthers"]},
    {"What is the nickname for Florida Gulf Coast University?": ["Eagles"]},
    {"What is the nickname for Florida Memorial University?": ["Lions"]},
    {"What is the nickname for Florida National University?": ["Conquistadors"]},
    {"What is the nickname for Florida Southern?": ["Moccasins"]},
    {"What is the nickname for Florida SouthWestern State College?": ["College Buccaneers"]},
    {"What is the nickname for Florida State College at Jacksonville?": ["Blue Wave"]},
    {"What is the nickname for Florida State University?": ["Seminoles"]},
    {"What is the nickname for Fordham University?": ["Rams"]},
    {"What is the nickname for Fort Hays State University?": ["Tigers"]},
    {"What is the nickname for Fort Valley State University?": ["Wildcats"]},
    {"What is the nickname for Francis Marion University?": ["Patriots"]},
    {"What is the nickname for Franklin University?": ["Raiders"]},
    {"What is the nickname for Franklin and Marshall College?": ["Diplomats"]},
    {"What is the nickname for Franklin College?": ["Grizzlies"]},
    {"What is the nickname for Freed-Hardeman University?": ["Lions", "Lady Lions"]},
    {"What is the nickname for Friends University?": ["Falcons"]},
    {"What is the nickname for Fresno Pacific University?": ["Sunbirds"]},
    {"What is the nickname for Fresno State?": ["Bulldogs"]},
    {"What is the nickname for Frostburg State University?": ["Bobcats"]},
    {"What is the nickname for Furman University?": ["Paladins"]},
    {"What is the nickname for Geneva College?": ["Golden Tornadoes"]},
    {"What is the nickname for Gannon University?": ["Golden Knights"]},
    {"What is the nickname for Genesee Community College?": ["Cougars"]},
    {"What is the nickname for George Mason University?": ["Patriots"]},
    {"What is the nickname for George Washington University?": ["Colonials"]},
    {"What is the nickname for Georgetown College?": ["Tigers"]},
    {"What is the nickname for Georgetown University?": ["Hoyas"]},
    {"What is the nickname for Georgia?": ["Bulldogs"]},
    {"What is the nickname for Georgia Gwinnett College?": ["Grizzlies"]},
    {"What is the nickname for Georgia Southern University?": ["Eagles", "Lady Eagles"]},
    {"What is the nickname for Georgia State University?": ["Panthers"]},
    {"What is the nickname for Georgia Tech?": ["Yellow Jackets"]},
    {"What is the nickname for Georgian Court University?": ["Lions"]},
    {"What is the nickname for Gettysburg College?": ["Bullets"]},
    {"What is the nickname for Glenville State College?": ["Pioneers", "Lady Pioneers"]},
    {"What is the nickname for Gonzaga University?": ["Bulldogs"]},
    {"What is the nickname for Gordon College?": ["Fighting Scots"]},
    {"What is the nickname for Goshen College?": ["Maple Leafs"]},
    {"What is the nickname for Grace College?": ["Lancers"]},
    {"What is the nickname for Graceland University?": ["Yellow Jackets"]},
    {"What is the nickname for Grambling State University?": ["Tigers", "Lady Tigers"]},
    {"What is the nickname for Grand Canyon University?": ["Lopes"]},
    {"What is the nickname for Grand Valley State University?": ["Lakers"]},
    {"What is the nickname for Grand View University?": ["Vikings"]},
    {"What is the nickname for Wisconsin-Green Bay?": ["Phoenix"]},
    {"What is the nickname for Greensboro College?": ["Pride"]},
    {"What is the nickname for Grinnell College?": ["Pioneers"]},
    {"What is the nickname for Guilford College?": ["Quakers"]},
    {"What is the nickname for Gulf Coast State College?": ["Commodores"]},
    {"What is the nickname for Gustavus Adolphus College?": ["Golden Gusties"]},
    {"What is the nickname for Hanover College?": ["Panthers"]},
    {"What is the nickname for Hampton University?": ["Pirates"]},
    {"What is the nickname for Hamilton College?": ["Continentals"]},
    {"What is the nickname for Harding University?": ["Bison"]},
    {"What is the nickname for Harris–Stowe State University?": ["Hornets"]},
    {"What is the nickname for University of Hartford?": ["Hawks"]},
    {"What is the nickname for Harvard University?": ["Crimson"]},
    {"What is the nickname for Hastings College?": ["Broncos"]},
    {"What is the nickname for Hawaii?": ["Rainbow Warriors", "Rainbows", "Warriors", "Rainbow Wahine"]},
    {"What is the nickname for Hawaii-Hilo?": ["Vulcans"]},
    {"What is the nickname for Heidelberg University?": ["Student Princes"]},
    {"What is the nickname for Henderson State University?": ["Reddies"]},
    {"What is the nickname for Hendrix College?": ["Warriors"]},
    {"What is the nickname for Herkimer County Community College?": ["Generals"]},
    {"What is the nickname for High Point University?": ["Panthers"]},
    {"What is the nickname for Hillsborough?": ["Hawks"]},
    {"What is the nickname for Hiram College?": ["Terriers"]},
    {"What is the nickname for Hobart College?": ["Statesmen"]},
    {"What is the nickname for Hofstra University?": ["Pride"]},
    {"What is the nickname for Hope College?": ["Flying Dutchmen"]},
    {"What is the nickname for Holy Cross College?": ["Crusaders"]},
    {"What is the nickname for Houston?": ["Cougars"]},
    {"What is the nickname for University of Houston–Downtown?": ["Gators"]},
    {"What is the nickname for University of Houston–Victoria?": ["Jaguars"]},
    {"What is the nickname for Howard University?": ["Bison"]},
    {"What is the nickname for Humboldt State University?": ["Lumberjacks"]},
    {"What is the nickname for Huntington University?": ["Foresters"]},
    {"What is the nickname for Idaho?": ["Vandals"]},
    {"What is the nickname for Idaho State University?": ["Bengals"]},
    {"What is the nickname for College of Idaho?": ["Coyotes"]},
    {"What is the nickname for Illinois Institute of Technology?": ["Scarlet Hawks"]},
    {"What is the nickname for Illinois?": ["Fighting Illini"]},
    {"What is the nickname for Illinois-Chicago?": ["Flames"]},
    {"What is the nickname for University of Illinois at Springfield?": ["Prairie Stars"]},
    {"What is the nickname for Illinois College?": ["Blue Boys", "Lady Blues"]},
    {"What is the nickname for Illinois State University?": ["Redbirds"]},
    {"What is the nickname for Illinois Wesleyan University?": ["Titans"]},
    {"What is the nickname for Incarnate Word College?": ["Cardinals"]},
    {"What is the nickname for Indian River State College?": ["Pioneers"]},
    {"What is the nickname for Indiana University?": ["Hoosiers"]},
    {"What is the nickname for Indiana State University?": ["Sycamores"]},
    {"What is the nickname for Indianapolis University?": ["Greyhounds"]},
    {"What is the nickname for Indiana University-Purdue University Fort Wayne?": ["Mastodons"]},
    {"What is the nickname for Indiana University-Purdue University Indianapolis?": ["Jaguars"]},
    {"What is the nickname for Indiana University of Pennsylvania?": ["Crimson Hawks"]},
    {"What is the nickname for Indiana University Southeast?": ["Grenadiers"]},
    {"What is the nickname for Indiana Wesleyan University?": ["Wildcats"]},
    {"What is the nickname for Iona College?": ["Gaels"]},
    {"What is the nickname for Iowa?": ["Hawkeyes"]},
    {"What is the nickname for Iowa State University?": ["Cyclones"]},
    {"What is the nickname for Iowa Wesleyan College?": ["Tigers"]},
    {"What is the nickname for Ithaca College?": ["Bombers"]},
    {"What is the nickname for Jackson State University?": ["Tigers", "Lady Tigers"]},
    {"What is the nickname for Jacksonville University?": ["Dolphins"]},
    {"What is the nickname for Jacksonville State University?": ["Gamecocks"]},
    {"What is the nickname for James Madison University?": ["Dukes"]},
    {"What is the nickname for Jamestown College?": ["Jimmies"]},
    {"What is the nickname for John Brown University?": ["Golden Eagles"]},
    {"What is the nickname for John Carroll University?": ["Blue Streaks"]},
    {"What is the nickname for Johns Hopkins University?": ["Blue Jays"]},
    {"What is the nickname for John Jay College?": ["Bloodhounds"]},
    {"What is the nickname for Johnson and Wales University?": ["Wildcats"]},
    {"What is the nickname for Johnson C. Smith University?": ["Golden Bulls"]},
    {"What is the nickname for Judson University?": ["Eagles"]},
    {"What is the nickname for Johnson University Florida?": ["Suns"]},
    {"What is the nickname for Kalamazoo College?": ["Fighting Hornets"]},
    {"What is the nickname for Kansas?": ["Jayhawks"]},
    {"What is the nickname for Kansas State University?": ["Wildcats"]},
    {"What is the nickname for Kansas Wesleyan University?": ["Coyotes"]},
    {"What is the nickname for Kean University?": ["Cougars"]},
    {"What is the nickname for Keene State College?": ["Owls"]},
    {"What is the nickname for Keiser University?": ["Sea Hawks"]},
    {"What is the nickname for Kennesaw State University?": ["Owls", "Lady Owls"]},
    {"What is the nickname for Kent State University?": ["Golden Flashes"]},
    {"What is the nickname for Kentucky?": ["Wildcats"]},
    {"What is the nickname for Kentucky Christian University?": ["Knights"]},
    {"What is the nickname for Kentucky State University?": ["Thorobreds", "Thorobrettes"]},
    {"What is the nickname for Kentucky Wesleyan College?": ["Panthers"]},
    {"What is the nickname for Kenyon College?": ["Lords", "Ladies"]},
    {"What is the nickname for King University?": ["Tornado"]},
    {"What is the nickname for Knox College?": ["Prairie Fire"]},
    {"What is the nickname for Kutztown University?": ["Golden Bears"]},
    {"What is the nickname for La Salle University?": ["Explorers"]},
    {"What is the nickname for LaGrange College?": ["Panthers"]},
    {"What is the nickname for Lafayette College?": ["Leopards"]},
    {"What is the nickname for Lake Erie College?": ["Storm"]},
    {"What is the nickname for Lake Forest College?": ["Foresters"]},
    {"What is the nickname for Lake-Sumter State College?": ["Lakers"]},
    {"What is the nickname for Lake Superior State University?": ["Lakers"]},
    {"What is the nickname for Lamar University?": ["Cardinals", "Lady Cardinals"]},
    {"What is the nickname for Langston University?": ["Lions", "Lady Lions"]},
    {"What is the nickname for Lawrence University?": ["Vikings"]},
    {"What is the nickname for Le Moyne College?": ["Dolphins"]},
    {"What is the nickname for Lebanon Valley College?": ["Flying Dutchmen"]},
    {"What is the nickname for Leech Lake?": ["Lakers"]},
    {"What is the nickname for Lehigh University?": ["Mountain Hawks"]},
    {"What is the nickname for LeMoyne-Owen College?": ["Magicians"]},
    {"What is the nickname for Lesley University?": ["Lynx"]},
    {"What is the nickname for Liberty University?": ["Flames", "Lady Flames"]},
    {"What is the nickname for Life University?": ["Running Eagles"]},
    {"What is the nickname for Lincoln Christian College?": ["Preachers", "Angels"]},
    {"What is the nickname for Lincoln University, Missouri?": ["Blue Tigers"]},
    {"What is the nickname for Lincoln University, Pennsylvania?": ["Lions"]},
    {"What is the nickname for Lincoln Memorial University?": ["Railsplitters"]},
    {"What is the nickname for Lindenwood University?": ["Lions"]},
    {"What is the nickname for Lindsey Wilson College?": ["Blue Raiders"]},
    {"What is the nickname for Linfield College?": ["Wildcats"]},
    {"What is the nickname for Lipscomb University?": ["Bisons", "Lady Bisons"]},
    {"What is the nickname for Livingstone College?": ["Blue Bears"]},
    {"What is the nickname for Lock Haven University?": ["Bald Eagles"]},
    {"What is the nickname for Longwood University?": ["Lancers"]},
    {"What is the nickname for Loras College?": ["Duhawks"]},
    {"What is the nickname for Los Angeles City College?": ["Cubs"]},
    {"What is the nickname for Los Angeles Harbor College?": ["Seahawks"]},
    {"What is the nickname for Los Angeles Mission College?": ["Eagles"]},
    {"What is the nickname for Los Angeles Pierce College?": ["Brahmas"]},
    {"What is the nickname for Los Angeles Southwest College?": ["Cougars"]},
    {"What is the nickname for Los Angeles Trade-Technical College?": ["Beavers"]},
    {"What is the nickname for Los Angeles Valley College?": ["Monarchs"]},
    {"What is the nickname for Louisiana Tech University?": ["Bulldogs", "Lady Techsters"]},
    {"What is the nickname for Louisiana-Lafayette?": ["Ragin' Cajuns"]},
    {"What is the nickname for Louisiana-Monroe?": ["Warhawks"]},
    {"What is the nickname for Louisiana State University?": ["Tigers", "Lady Tigers"]},
    {"What is the nickname for Louisiana State University of Alexandria?": ["Generals"]},
    {"What is the nickname for Louisville?": ["Cardinals"]},
    {"What is the nickname for Loyola University of Chicago?": ["Ramblers"]},
    {"What is the nickname for Loyola University of Maryland?": ["Greyhounds"]},
    {"What is the nickname for Loyola Marymount University?": ["Lions"]},
    {"What is the nickname for Loyola University of New Orleans?": ["Wolfpack"]},
    {"What is the nickname for Loyola University of Los Angeles?": ["Lions"]},
    {"What is the nickname for Lubbock Christian University?": ["Chaparrals"]},
    {"What is the nickname for Luther College?": ["Norse"]},
    {"What is the nickname for Lyndon State College?": ["Hornets"]},
    {"What is the nickname for Lynn?": ["Fighting Knights"]},
    {"What is the nickname for Macalester College?": ["Scots"]},
    {"What is the nickname for MacMurray College?": ["Highlanders"]},
    {"What is the nickname for Maine?": ["Black Bears"]},
    {"What is the nickname for Malone University?": ["Pioneers"]},
    {"What is the nickname for Stage College of Florida Manatee?": ["Manatees"]},
    {"What is the nickname for Manchester College?": ["Spartans"]},
    {"What is the nickname for Manhattan College?": ["Jaspers", "Lady Jaspers"]},
    {"What is the nickname for Mansfield University of Pennsylvania?": ["Mountaineers"]},
    {"What is the nickname for Marietta College?": ["Pioneers"]},
    {"What is the nickname for Marist College?": ["Red Foxes"]},
    {"What is the nickname for Marquette University?": ["Golden Eagles"]},
    {"What is the nickname for Marshall University?": ["Thundering Herd"]},
    {"What is the nickname for Mary Baldwin College?": ["Fighting Squirrels"]},
    {"What is the nickname for Maryland?": ["Terrapins"]},
    {"What is the nickname for University of Maryland, Baltimore County?": ["Retrievers"]},
    {"What is the nickname for Marywood University?": ["Pacers"]},
    {"What is the nickname for Massachusetts?": ["Minutemen"]},
    {"What is the nickname for Massachusetts-Boston?": ["Beacons"]},
    {"What is the nickname for Massachusetts-Lowell?": ["River Hawks"]},
    {"What is the nickname for Massachusetts Institute of Technology?": ["Engineers"]},
    {"What is the nickname for The Masters University?": ["Mustangs"]},
    {"What is the nickname for McDaniel College?": ["Green Terror"]},
    {"What is the nickname for McNeese State University?": ["Cowboys", "Cowgirls"]},
    {"What is the nickname for McMurry University?": ["Indians"]},
    {"What is the nickname for McPherson College?": ["Bulldogs"]},
    {"What is the nickname for Medaille College?": ["Mavericks"]},
    {"What is the nickname for Memphis?": ["Tigers", "Lady Tigers"]},
    {"What is the nickname for Mercer University?": ["Bears"]},
    {"What is the nickname for Mercyhurst College?": ["Lakers"]},
    {"What is the nickname for Messiah College?": ["Falcons"]},
    {"What is the nickname for Metropolitan State University of Denver?": ["Roadrunners"]},
    {"What is the nickname for Miami?": ["Hurricanes"]},
    {"What is the nickname for Miami-Dade?": ["Sharks"]},
    {"What is the nickname for Miami University, Ohio?": ["RedHawks"]},
    {"What is the nickname for Michigan?": ["Wolverines"]},
    {"What is the nickname for Michigan State University?": ["Spartans"]},
    {"What is the nickname for Michigan Technological University?": ["Huskies"]},
    {"What is the nickname for MidAmerica Nazarene University?": ["Pioneers"]},
    {"What is the nickname for Middle Tennessee State University?": ["Blue Raiders"]},
    {"What is the nickname for Middlebury College?": ["Panthers"]},
    {"What is the nickname for Midland University?": ["Warriors"]},
    {"What is the nickname for Midwestern State University?": ["Mustangs", "Lady Mustangs"]},
    {"What is the nickname for Mills College?": ["Cyclones"]},
    {"What is the nickname for Milligan College?": ["Buffaloes"]},
    {"What is the nickname for Millsaps College?": ["Majors"]},
    {"What is the nickname for Millersville College?": ["Marauders"]},
    {"What is the nickname for Minnesota?": ["Golden Gophers"]},
    {"What is the nickname for Minnesota-Crookston?": ["Golden Eagles"]},
    {"What is the nickname for Minnesota-Duluth?": ["Bulldogs"]},
    {"What is the nickname for Minnesota-Morris?": ["Cougars"]},
    {"What is the nickname for Minnesota State?": ["Mavericks"]},
    {"What is the nickname for Minnesota State University-Moorhead?": ["Dragons"]},
    {"What is the nickname for Misericordia University?": ["Cougars"]},
    {"What is the nickname for Mississippi?": ["Rebels"]},
    {"What is the nickname for Mississippi College?": ["Choctaws"]},
    {"What is the nickname for Mississippi State University?": ["Bulldogs", "Lady Bulldogs"]},
    {"What is the nickname for Mississippi Valley State University?": ["Delta Devils", "Devilettes"]},
    {"What is the nickname for Missouri?": ["Tigers"]},
    {"What is the nickname for Missouri-Kansas City?": ["Kangaroos"]},
    {"What is the nickname for Missouri-St Louis?": ["Tritons"]},
    {"What is the nickname for Missouri-Rolla?": ["Engineers"]},
    {"What is the nickname for Missouri Southern State University?": ["Lions"]},
    {"What is the nickname for Missouri Western State University?": ["Griffons"]},
    {"What is the nickname for Missouri State University?": ["Bears", "Lady Bears"]},
    {"What is the nickname for Missouri Valley College?": ["Vikings"]},
    {"What is the nickname for Massachusetts Institute of Technology?": ["Engineers"]},
    {"What is the nickname for Mobile University?": ["Rams"]},
    {"What is the nickname for Monmouth University?": ["Hawks"]},
    {"What is the nickname for Montana?": ["Grizzlies"]},
    {"What is the nickname for Montana State University?": ["Bobcats"]},
    {"What is the nickname for Montclair State University?": ["Red Hawks"]},
    {"What is the nickname for University of Montevallo?": ["Falcons"]},
    {"What is the nickname for Moravian College?": ["Greyhounds"]},
    {"What is the nickname for Morehead State University?": ["Eagles"]},
    {"What is the nickname for Morgan State University?": ["Bears", "Lady Bears"]},
    {"What is the nickname for Morningside College?": ["Mustangs"]},
    {"What is the nickname for Morrisville State College?": ["Mustangs"]},
    {"What is the nickname for Mount Mercy College?": ["Mustangs"]},
    {"What is the nickname for Mount St. Mary's University?": ["Mountaineers"]},
    {"What is the nickname for Mount Union College?": ["Purple Raiders"]},
    {"What is the nickname for Muhlenberg College?": ["Mules"]},
    {"What is the nickname for Murray State University?": ["Racers", "Lady Racers"]},
    {"What is the nickname for Muskingum University?": ["Fighting Muskies"]},
    {"What is the nickname for Navy?": ["Midshipmen"]},
    {"What is the nickname for Nebraska?": ["Cornhuskers"]},
    {"What is the nickname for Nebraska-Kearney?": ["Lopers"]},
    {"What is the nickname for Nebraska-Omaha?": ["Mavericks"]},
    {"What is the nickname for Nebraska Wesleyan University?": ["Prairie Wolves"]},
    {"What is the nickname for Nevada?": ["Wolf Pack"]},
    {"What is the nickname for University of Nevada, Las Vegas?": ["Rebels", "Runnin' Rebels", "Lady Rebels"]},
    {"What is the nickname for University of New England, Maine?": ["Nor'easters"]},
    {"What is the nickname for New Hampshire?": ["Wildcats"]},
    {"What is the nickname for New Haven?": ["Chargers"]},
    {"What is the nickname for New Jersey Institute of Technology?": ["Highlanders"]},
    {"What is the nickname for New Mexico?": ["Lobos"]},
    {"What is the nickname for New Mexico State University?": ["Aggies"]},
    {"What is the nickname for New Mexico Mining and Technology?": ["Pygmies"]},
    {"What is the nickname for New Orleans?": ["Privateers and Lady Privateers"]},
    {"What is the nickname for New York University?": ["Violets"]},
    {"What is the nickname for Niagara University?": ["Purple Eagles"]},
    {"What is the nickname for Nicholls State University?": ["Colonels"]},
    {"What is the nickname for Norfolk State University?": ["Spartans"]},
    {"What is the nickname for North Alabama?": ["Lions"]},
    {"What is the nickname for University of North Carolina, Asheville?": ["Bulldogs"]},
    {"What is the nickname for North Carolina?": ["Tar Heels"]},
    {"What is the nickname for University of North Carolina, Charlotte?": ["49ers"]},
    {"What is the nickname for University of North Carolina, Greensboro?": ["Spartans"]},
    {"What is the nickname for University of North Carolina, Pembroke?": ["Braves"]},
    {"What is the nickname for University of North Carolina, Wilmington?": ["Seahawks"]},
    {"What is the nickname for North Carolina A and T University?": ["Aggies"]},
    {"What is the nickname for North Carolina Central University?": ["Eagles"]},
    {"What is the nickname for North Carolina School of the Arts?": ["Fighting Pickles"]},
    {"What is the nickname for North Carolina State University?": ["Wolfpack"]},
    {"What is the nickname for North Dakota?": ["Fighting Hawks"]},
    {"What is the nickname for North Dakota State University?": ["Bison"]},
    {"What is the nickname for North Georgia?": ["Nighthawks"]},
    {"What is the nickname for North Florida?": ["Ospreys"]},
    {"What is the nickname for North Park University?": ["Vikings"]},
    {"What is the nickname for North Texas?": ["Mean Green"]},
    {"What is the nickname for Northeastern University, Boston?": ["Huskies"]},
    {"What is the nickname for Northeastern State University?": ["Riverhawks"]},
    {"What is the nickname for Northern Arizona University?": ["Lumberjacks"]},
    {"What is the nickname for Northern Colorado?": ["Bears"]},
    {"What is the nickname for Northern Illinois University?": ["Huskies"]},
    {"What is the nickname for Northern Iowa?": ["Panthers"]},
    {"What is the nickname for Northern Kentucky University?": ["Norse"]},
    {"What is the nickname for Northrop University?": ["Black Knights"]},
    {"What is the nickname for Northern Michigan University?": ["Wildcats"]},
    {"What is the nickname for Northern New Mexico College?": ["Eagles"]},
    {"What is the nickname for Northwest Christian University?": ["Beacons"]},
    {"What is the nickname for Northwest Florida?": ["Raiders"]},
    {"What is the nickname for Northwest Missouri State University?": ["Bearcats"]},
    {"What is the nickname for Northwestern University?": ["Wildcats"]},
    {"What is the nickname for Northwestern State University?": ["Demons", "Lady Demons"]},
    {"What is the nickname for Norwich University?": ["Cadets"]},
    {"What is the nickname for Notre Dame?": ["Fighting Irish"]},
    {"What is the nickname for Nova Southeastern University?": ["Sharks"]},
    {"What is the nickname for Oak Hills Christian College?": ["Wolfpack"]},
    {"What is the nickname for Oakland University?": ["Golden Grizzlies"]},
    {"What is the nickname for Oakton Community College?": ["Raiders"]},
    {"What is the nickname for Oberlin College?": ["Yeomen"]},
    {"What is the nickname for Occidental College?": ["Tigers"]},
    {"What is the nickname for Oglethorpe University?": ["Stormy Petrels"]},
    {"What is the nickname for Ohio University?": ["Bobcats"]},
    {"What is the nickname for Ohio Northern University?": ["Polar Bears"]},
    {"What is the nickname for Ohio State University?": ["Buckeyes"]},
    {"What is the nickname for Ohio Valley University?": ["Fighting Scots"]},
    {"What is the nickname for Ohio Wesleyan University?": ["Battlin' Bishops"]},
    {"What is the nickname for Oklahoma?": ["Sooners"]},
    {"What is the nickname for Oklahoma City University?": ["Stars"]},
    {"What is the nickname for Oklahoma State University?": ["Cowboys", "Cowgirls"]},
    {"What is the nickname for Oklahoma Panhandle State University?": ["Aggies"]},
    {"What is the nickname for Oklahoma Wesleyan University?": ["Eagles"]},
    {"What is the nickname for Ole Miss?": ["Rebels"]},
    {"What is the nickname for Old Dominion University?": ["Monarchs", "Lady Monarchs"]},
    {"What is the nickname for Olivet Nazarene University?": ["Tigers"]},
    {"What is the nickname for Oral Roberts University?": ["Golden Eagles"]},
    {"What is the nickname for Oregon?": ["Ducks"]},
    {"What is the nickname for Oregon State University?": ["Beavers"]},
    {"What is the nickname for Oregon Institute of Technology?": ["Hustlin' Owls"]},
    {"What is the nickname for Oswego State University?": ["Great Lakers"]},
    {"What is the nickname for Ouachita Baptist University?": ["Tigers"]},
    {"What is the nickname for College of the Ozarks?": ["Bobcats"]},
    {"What is the nickname for The Ozarks?": ["Eagles"]},
    {"What is the nickname for Pace University?": ["Setters"]},
    {"What is the nickname for Pacific?": ["Tigers"]},
    {"What is the nickname for Pacific University?": ["Boxers"]},
    {"What is the nickname for Pacific Lutheran University?": ["Lutes"]},
    {"What is the nickname for Palm Beach Atlantic?": ["Sailfish"]},
    {"What is the nickname for Palm Beach State College?": ["Panthers"]},
    {"What is the nickname for Park University?": ["Pirates"]},
    {"What is the nickname for Pasadena City College?": ["Lancers"]},
    {"What is the nickname for Pasco–Hernando State College?": ["Conquistadors"]},
    {"What is the nickname for Pensacola Christian College?": ["Eagles"]},
    {"What is the nickname for Pensacola State College?": ["Pirates"]},
    {"What is the nickname for Pennsylvania?": ["Quakers"]},
    {"What is the nickname for Pennsylvania State University Nittany?": ["Lions", "Lady Lions"]},
    {"What is the nickname for Pepperdine University?": ["Waves"]},
    {"What is the nickname for University of Pikeville?": ["Bears"]},
    {"What is the nickname for Pittsburg State University?": ["Gorillas"]},
    {"What is the nickname for Pittsburgh?": ["Panthers"]},
    {"What is the nickname for Pittsburgh-Bradford?": ["Panthers"]},
    {"What is the nickname for Pittsburgh-Greensburg?": ["Bobcats"]},
    {"What is the nickname for Pittsburgh-Johnstown?": ["Mountain Cats"]},
    {"What is the nickname for Pittsburgh-Titusville?": ["Panthers"]},
    {"What is the nickname for Pitzer College?": ["Sagehens"]},
    {"What is the nickname for Point Loma Nazarene University?": ["Sea Lions"]},
    {"What is the nickname for Point Park University Pittsburgh, Pennsylvania?": ["Pioneers"]},
    {"What is the nickname for Point University?": ["Skyhawks"]},
    {"What is the nickname for Polk State College?": ["Eagles"]},
    {"What is the nickname for Pomona College?": ["Sagehens"]},
    {"What is the nickname for Portland?": ["Pilots"]},
    {"What is the nickname for Portland State University?": ["Vikings"]},
    {"What is the nickname for Post University?": ["Eagles"]},
    {"What is the nickname for Prairie View A&M University?": ["Panthers", "Lady Panthers"]},
    {"What is the nickname for Presbyterian College?": ["Blue Hose"]},
    {"What is the nickname for Princeton University?": ["Tigers"]},
    {"What is the nickname for Providence College?": ["Friars"]},
    {"What is the nickname for Puerto Rico?": ["Tarzans", "Janes"]},
    {"What is the nickname for Purdue University?": ["Boilermakers"]},
    {"What is the nickname for Purdue-Calumet?": ["Peregrines"]},
    {"What is the nickname for Purdue-Ft. Wayne?": ["Mastodons"]},
    {"What is the nickname for Quinnipiac University?": ["Bobcats"]},
    {"What is the nickname for Quincy University?": ["Hawks"]},
    {"What is the nickname for Radford University?": ["Highlanders"]},
    {"What is the nickname for Randolph-Macon College?": ["Yellow Jackets"]},
    {"What is the nickname for Redlands?": ["Bulldogs"]},
    {"What is the nickname for Reed College?": ["Griffins"]},
    {"What is the nickname for Regis University?": ["Rangers"]},
    {"What is the nickname for Reinhardt University?": ["Eagles"]},
    {"What is the nickname for Rensselaer Polytechnic Institute?": ["Engineers"]},
    {"What is the nickname for Rhema College?": ["Eagles"]},
    {"What is the nickname for Richmond?": ["Spiders"]},
    {"What is the nickname for Rice University?": ["Owls"]},
    {"What is the nickname for Rider University?": ["Broncs"]},
    {"What is the nickname for Rhode Island?": ["Rams"]},
    {"What is the nickname for Rhode Island College?": ["Anchormen"]},
    {"What is the nickname for Rhode Island School of Design?": ["Nads"]},
    {"What is the nickname for Rhodes College?": ["Lynx"]},
    {"What is the nickname for Roanoke College?": ["Maroons"]},
    {"What is the nickname for Rochester?": ["Yellow Jackets"]},
    {"What is the nickname for Robert Morris, Pennsylvania?": ["Colonials"]},
    {"What is the nickname for Robert Morris University, Illinois?": ["Eagles"]},
    {"What is the nickname for Rochester Institute of Technology?": ["Tigers"]},
    {"What is the nickname for Rock Valley College?": ["Golden Eagles"]},
    {"What is the nickname for Rockford University?": ["Regents"]},
    {"What is the nickname for Rollins College?": ["Tars"]},
    {"What is the nickname for Rose-Hulman Institute of Technology?": ["Fightin Engineers"]},
    {"What is the nickname for Rosemont College?": ["Ravens"]},
    {"What is the nickname for Rowan University?": ["Profs"]},
    {"What is the nickname for Rutgers University?": ["Scarlet Knights"]},
    {"What is the nickname for Rutgers–Camden?": ["Scarlet Raptors"]},
    {"What is the nickname for Rutgers–Newark?": ["Scarlet Raiders"]},
    {"What is the nickname for Sacramento State University?": ["Hornets"]},
    {"What is the nickname for Sacred Heart University?": ["Pioneers"]},
    {"What is the nickname for Saint Ambrose University?": ["Fighting Bees", "Queen Bees"]},
    {"What is the nickname for Saint Anselm College?": ["Hawks"]},
    {"What is the nickname for Saint Benedicts College?": ["Blazers"]},
    {"What is the nickname for Saint Bonaventure University?": ["Bonnies"]},
    {"What is the nickname for Saint Cloud State University?": ["Huskies"]},
    {"What is the nickname for Saint Edwards University?": ["Hilltoppers"]},
    {"What is the nickname for Saint Francis, Indiana?": ["Cougars"]},
    {"What is the nickname for Saint Francis College, New York?": ["Terriers"]},
    {"What is the nickname for Saint Francis University?": ["Red Flash"]},
    {"What is the nickname for Saint John Fisher?": ["Cardinals"]},
    {"What is the nickname for St. Johns River?": ["Vikings"]},
    {"What is the nickname for Saint Johns University, Minnesota?": ["Johnnies"]},
    {"What is the nickname for Saint Johns University, New York?": ["Red Storm"]},
    {"What is the nickname for Saint Josephs College, Indiana?": ["Pumas"]},
    {"What is the nickname for Saint Josephs College, New York City?": ["Bears", "Lady Bears"]},
    {"What is the nickname for Saint Josephs College on Long Island?": ["Golden Eagles", "Lady Eagles"]},
    {"What is the nickname for Saint Josephs University?": ["Hawks"]},
    {"What is the nickname for Saint Lawrence University?": ["Saints"]},
    {"What is the nickname for Saint Leo Lions?": ["Saint Leo Lions"]},
    {"What is the nickname for Saint Louis University?": ["Billikens"]},
    {"What is the nickname for Saint Louis College of Pharmacy?": ["Eutectics"]},
    {"What is the nickname for Saint Mary?": ["Spires"]},
    {"What is the nickname for Saint Marys College of California?": ["Gaels"]},
    {"What is the nickname for Saint Marys University of Minnesota?": ["Cardinals"]},
    {"What is the nickname for Saint Mary-of-the-Woods College?": ["Pomeroys"]},
    {"What is the nickname for Saint Michaels College?": ["Purple Knights"]},
    {"What is the nickname for Saint Olaf College?": ["Oles"]},
    {"What is the nickname for St. Petersburg College?": ["Titans"]},
    {"What is the nickname for Saint Peters University?": ["Peacocks", "Peahens"]},
    {"What is the nickname for St. Thomas University Florida?": ["Bobcats"]},
    {"What is the nickname for Saint Thomas, Minnesota?": ["Tommies"]},
    {"What is the nickname for Saint Vincent College Latrobe, Pennsylvania?": ["Bearcats"]},
    {"What is the nickname for Saint Xavier University?": ["Cougars"]},
    {"What is the nickname for Salem International University?": ["Tigers"]},
    {"What is the nickname for Salem State University?": ["Vikings"]},
    {"What is the nickname for Salisbury University?": ["Seagulls"]},
    {"What is the nickname for Sam Houston State University?": ["Bearkats"]},
    {"What is the nickname for Samford University?": ["Bulldogs"]},
    {"What is the nickname for University of San Diego?": ["Toreros"]},
    {"What is the nickname for San Diego State University?": ["Aztecs"]},
    {"What is the nickname for San Francisco?": ["Dons"]},
    {"What is the nickname for San Jose State University?": ["Spartans"]},
    {"What is the nickname for Santa Clara University?": ["Broncos"]},
    {"What is the nickname for Santa Fe College?": ["Saints"]},
    {"What is the nickname for Savannah College of Art and Design?": ["Bees"]},
    {"What is the nickname for Savannah State University?": ["Tigers", "Lady Tigers"]},
    {"What is the nickname for Scottsdale Community College?": ["Artichokes"]},
    {"What is the nickname for Seattle University?": ["Redhawks"]},
    {"What is the nickname for Seattle Pacific University?": ["Falcons"]},
    {"What is the nickname for Seton Hall University?": ["Pirates"]},
    {"What is the nickname for Seton Hill University Greensburg, Pennsylvania?": ["Griffins"]},
    {"What is the nickname for Sewanee, The University of the South?": ["Tigers"]},
    {"What is the nickname for Siena College?": ["Saints"]},
    {"What is the nickname for Simmons College of Kentucky?": ["Panthers"]},
    {"What is the nickname for Simon's Rock College?": ["Llamas"]},
    {"What is the nickname for Simpson College?": ["Storm"]},
    {"What is the nickname for Shawnee State University?": ["Bears"]},
    {"What is the nickname for Shepherd University?": ["Rams"]},
    {"What is the nickname for Shimer College?": ["Flaming Smelts"]},
    {"What is the nickname for Shippensburg University of Pennsylvania?": ["Red Raiders"]},
    {"What is the nickname for Skidmore College?": ["Thoroughbreds"]},
    {"What is the nickname for Slippery Rock University?": ["The Rock"]},
    {"What is the nickname for South Alabama?": ["Jaguars"]},
    {"What is the nickname for South Carolina?": ["Gamecocks"]},
    {"What is the nickname for University of South Carolina Beaufort?": ["Sand Sharks"]},
    {"What is the nickname for South Carolina Upstate?": ["Spartans"]},
    {"What is the nickname for South Carolina State University?": ["Bulldogs"]},
    {"What is the nickname for South Dakota?": ["Coyotes"]},
    {"What is the nickname for South Dakota School of Mines and Technology?": ["Hardrockers"]},
    {"What is the nickname for South Dakota State University?": ["Jackrabbits"]},
    {"What is the nickname for South Florida?": ["Bulls"]},
    {"What is the nickname for Southeast Missouri State University?": ["Redhawks"]},
    {"What is the nickname for Southeastern?": ["Fire"]},
    {"What is the nickname for Southeastern Louisiana University?": ["Lions", "Lady Lions"]},
    {"What is the nickname for Southeastern Oklahoma State University?": ["Savage Storm"]},
    {"What is the nickname for Southeastern University?": ["Fire"]},
    {"What is the nickname for Southern Arkansas University?": ["Muleriders", "Lady Muleriders"]},
    {"What is the nickname for Southern California?": ["Trojans", "Women of Troy"]},
    {"What is the nickname for Southern University and A and M College?": ["Jaguars"]},
    {"What is the nickname for Southern Connecticut State University?": ["Owls"]},
    {"What is the nickname for Southern Illinois University, Carbondale?": ["Salukis"]},
    {"What is the nickname for Southern Illinois University, Edwardsville?": ["Cougars"]},
    {"What is the nickname for Southern Indiana University?": ["Screaming Eagles"]},
    {"What is the nickname for Southern Maine?": ["Huskies"]},
    {"What is the nickname for Southern Methodist University?": ["Mustangs"]},
    {"What is the nickname for Southern Mississippi?": ["Golden Eagles"]},
    {"What is the nickname for Southern Nazarene University?": ["Crimson Storm"]},
    {"What is the nickname for Southern New Hampshire?": ["Penmen"]},
    {"What is the nickname for Southern Utah University?": ["Thunderbirds", "Lady Thunderbirds"]},
    {"What is the nickname for Southern Virginia University?": ["Knights"]},
    {"What is the nickname for Southwest Minnesota State University?": ["Mustangs"]},
    {"What is the nickname for Southwest Baptist University?": ["Bearcats"]},
    {"What is the nickname for Southwestern College?": ["Moundbuilders"]},
    {"What is the nickname for Southwestern University?": ["Pirates"]},
    {"What is the nickname for Spring Hill College?": ["Badgers"]},
    {"What is the nickname for Springfield College?": ["Pride"]},
    {"What is the nickname for Saint Thomas?": ["Bobcats"]},
    {"What is the nickname for Stanford University?": ["Cardinal"]},
    {"What is the nickname for College of Staten Island?": ["Dolphins"]},
    {"What is the nickname for Stephen F. Austin State University?": ["Lumberjacks", "Ladyjacks"]},
    {"What is the nickname for Stetson University?": ["Mad Hatters"]},
    {"What is the nickname for Stockton University?": ["Ospreys"]},
    {"What is the nickname for Stonehill College?": ["Skyhawks"]},
    {"What is the nickname for State University of New York at Buffalo?": ["Bulls"]},
    {"What is the nickname for State University of New York at Brockport?": ["Golden Eagles"]},
    {"What is the nickname for State University of New York at Cortland?": ["Red Dragons"]},
    {"What is the nickname for State University of New York at Environmental Science and Forestry?": ["Mighty Oaks"]},
    {"What is the nickname for State University of New York at Fredonia?": ["Blue Devils"]},
    {"What is the nickname for State University of New York at Geneseo?": ["Knights"]},
    {"What is the nickname for State University of New York at Institute of Technology?": ["Wildcats"]},
    {"What is the nickname for State University of New York at New Paltz?": ["Hawks"]},
    {"What is the nickname for State University of New York at Oneonta?": ["Red Dragons"]},
    {"What is the nickname for State University of New York at Plattsburgh?": ["Cardinals"]},
    {"What is the nickname for State University of New York at Potsdam?": ["Bears"]},
    {"What is the nickname for State University of New York at Stony Brook?": ["Seawolves"]},
    {"What is the nickname for Sussex County Community College?": ["Skylanders"]},
    {"What is the nickname for Sweet Briar?": ["Vixens"]},
    {"What is the nickname for Syracuse University?": ["Orange"]},
    {"What is the nickname for Tabor College?": ["Bluejays"]},
    {"What is the nickname for Tallahassee Community College?": ["Eagles"]},
    {"What is the nickname for Tampa?": ["Spartans"]},
    {"What is the nickname for Tarleton State University?": ["Texans", "Texanns"]},
    {"What is the nickname for Taylor University?": ["Trojans"]},
    {"What is the nickname for The College of New Jersey?": ["Lions"]},
    {"What is the nickname for Temple University?": ["Owls"]},
    {"What is the nickname for Tennessee?": ["Volunteers", "Lady Volunteers"]},
    {"What is the nickname for Tennessee-Chattanooga?": ["Mocs"]},
    {"What is the nickname for Tennessee-Martin?": ["Skyhawks"]},
    {"What is the nickname for Tennessee State University?": ["Tigers", "Lady Tigers"]},
    {"What is the nickname for Tennessee Tech?": ["Golden Eagles"]},
    {"What is the nickname for Tennessee Temple University?": ["Crusaders"]},
    {"What is the nickname for Texas?": ["Longhorns"]},
    {"What is the nickname for Texas-Arlington?": ["Mavericks"]},
    {"What is the nickname for Texas-Brownsville?": ["Ocelots"]},
    {"What is the nickname for Texas Christian University?": ["Horned Frogs"]},
    {"What is the nickname for Texas-Dallas?": ["Comets"]},
    {"What is the nickname for University of Texas at El Paso?": ["Miners"]},
    {"What is the nickname for Texas-Pan American?": ["Broncs", "Lady Broncs"]},
    {"What is the nickname for Texas-Permian Basin?": ["Falcons"]},
    {"What is the nickname for Texas Rio Grande Valley?": ["Vaqueros"]},
    {"What is the nickname for Texas-San Antonio?": ["Roadrunners"]},
    {"What is the nickname for Texas-Tyler?": ["Patriots"]},
    {"What is the nickname for Texas A and M University?": ["Aggies"]},
    {"What is the nickname for Texas A and M Commerce?": ["Lions"]},
    {"What is the nickname for Texas A and M Corpus Christi?": ["Islanders"]},
    {"What is the nickname for Texas A and M International?": ["Dustdevils"]},
    {"What is the nickname for Texas A and M Kingsville?": ["Javelinas"]},
    {"What is the nickname for Texas Lutheran University?": ["Bulldogs"]},
    {"What is the nickname for Texas Southern University?": ["Tigers"]},
    {"What is the nickname for Texas State University?": ["Bobcats"]},
    {"What is the nickname for Texas Tech University?": ["Red Raiders", "Lady Raiders"]},
    {"What is the nickname for Texas Wesleyan University?": ["Rams", "Lady Rams"]},
    {"What is the nickname for Thiel College Greenville, Pennsylvania?": ["Tomcats"]},
    {"What is the nickname for Thomas?": ["Night Hawks"]},
    {"What is the nickname for Thomas More College?": ["Blue Rebels"]},
    {"What is the nickname for Toccoa Falls College?": ["Eagles"]},
    {"What is the nickname for University of Toledo?": ["Rockets"]},
    {"What is the nickname for Towson State University?": ["Tigers"]},
    {"What is the nickname for Transylvania University?": ["Pioneers"]},
    {"What is the nickname for Trevecca Nazarene University?": ["Trojans"]},
    {"What is the nickname for Trine University?": ["Thunder"]},
    {"What is the nickname for Trinity Baptist?": ["Eagles"]},
    {"What is the nickname for Trinity Bible College?": ["Lions"]},
    {"What is the nickname for Trinity Christian College?": ["Trolls"]},
    {"What is the nickname for Trinity College Connecticut?": ["Bantams"]},
    {"What is the nickname for Trinity College Florida?": ["Tigers"]},
    {"What is the nickname for Trinity University Texas?": ["Tigers"]},
    {"What is the nickname for Troy University?": ["Trojans"]},
    {"What is the nickname for Truman State University?": ["Bulldogs"]},
    {"What is the nickname for Tufts University?": ["Jumbos"]},
    {"What is the nickname for Tulane University?": ["Green Wave"]},
    {"What is the nickname for Tulsa?": ["Golden Hurricane"]},
    {"What is the nickname for Turtle Mountain?": ["Mighty Mikinocks"]},
    {"What is the nickname for Tusculum College?": ["Pioneers"]},
    {"What is the nickname for Tuskegee University?": ["Golden Tigers", "Lady Tigers"]},
    {"What is the nickname for Union College Kentucky?": ["Bulldogs", "Lady Bulldogs"]},
    {"What is the nickname for Union College New York?": ["Dutchmen", "Dutchwomen"]},
    {"What is the nickname for Union University Tennessee?": ["Bulldogs", "Lady Bulldogs"]},
    {"What is the nickname for Utah?": ["Utes", "Runnin' Utes", "Red Rocks"]},
    {"What is the nickname for Upper Iowa University?": ["Peacocks"]},
    {"What is the nickname for Utah State University?": ["Aggies"]},
    {"What is the nickname for Utah Valley?": ["Wolverines"]},
    {"What is the nickname for Utica College?": ["Pioneers"]},
    {"What is the nickname for Valdosta State University?": ["Blazers"]},
    {"What is the nickname for Valparaiso University?": ["Crusaders"]},
    {"What is the nickname for Vanderbilt University?": ["Commodores"]},
    {"What is the nickname for Vassar College?": ["Brewers"]},
    {"What is the nickname for Vermont?": ["Catamounts"]},
    {"What is the nickname for Stevenson University?": ["Mustangs"]},
    {"What is the nickname for Villanova University?": ["Wildcats"]},
    {"What is the nickname for Vincennes University?": ["Trailblazers"]},
    {"What is the nickname for Virginia?": ["Cavaliers"]},
    {"What is the nickname for Virginia Commonwealth University?": ["Rams"]},
    {"What is the nickname for Virginia Military Institute?": ["Keydets"]},
    {"What is the nickname for Virginia State University?": ["Trojans"]},
    {"What is the nickname for Virginia Tech?": ["Hokies"]},
    {"What is the nickname for Virginia Union University?": ["Panthers"]},
    {"What is the nickname for Virginia Wesleyan College?": ["Marlins"]},
    {"What is the nickname for Viterbo University?": ["V Hawks"]},
    {"What is the nickname for Voorhees College?": ["Tigers"]},
    {"What is the nickname for Wabash College?": ["Little Giants"]},
    {"What is the nickname for Wagner?": ["Seahawks"]},
    {"What is the nickname for Wake Forest?": ["Demon Deacons"]},
    {"What is the nickname for Waldorf?": ["Warriors"]},
    {"What is the nickname for Walsh University?": ["Cavaliers"]},
    {"What is the nickname for Warner University?": ["Royals"]},
    {"What is the nickname for Wartburg?": ["Knights"]},
    {"What is the nickname for Washburn?": ["Ichabods", "Lady Blues"]},
    {"What is the nickname for University of Washington?": ["Huskies"]},
    {"What is the nickname for Washington University in Saint Louis?": ["Bears"]},
    {"What is the nickname for Washington and Jefferson?": ["Presidents"]},
    {"What is the nickname for Washington and Lee?": ["Generals"]},
    {"What is the nickname for Washington State University?": ["Cougars"]},
    {"What is the nickname for Wayland Baptist?": ["Pioneers"]},
    {"What is the nickname for Wayne State College?": ["Wildcats"]},
    {"What is the nickname for Wayne State University?": ["Warriors"]},
    {"What is the nickname for Webber International University?": ["Warriors"]},
    {"What is the nickname for Weber State University?": ["Wildcats"]},
    {"What is the nickname for Webster University?": ["Gorloks"]},
    {"What is the nickname for Wellesley College?": ["Blue"]},
    {"What is the nickname for Wentworth Institute of Technology?": ["Leopards"]},
    {"What is the nickname for Wesley College?": ["Wolverines"]},
    {"What is the nickname for Wesleyan?": ["Cardinals"]},
    {"What is the nickname for West Alabama?": ["Tigers"]},
    {"What is the nickname for West Chester?": ["Golden Rams"]},
    {"What is the nickname for West Florida?": ["Argonauts"]},
    {"What is the nickname for West Georgia?": ["Wolves"]},
    {"What is the nickname for West Liberty State?": ["Hilltoppers", "Lady Toppers"]},
    {"What is the nickname for West Texas A and M?": ["Buffaloes"]},
    {"What is the nickname for West Los Angeles College?": ["Wildcats"]},
    {"What is the nickname for West Virginia?": ["Mountaineers"]},
    {"What is the nickname for West Virginia State University?": ["Yellow Jackets"]},
    {"What is the nickname for West Virginia University at Parkersburg?": ["Riverhawks"]},
    {"What is the nickname for West Virginia Tech?": ["Golden Bears", "Lady Golden Bears"]},
    {"What is the nickname for West Virginia Wesleyan?": ["Bobcats", "Lady Bobcats"]},
    {"What is the nickname for Western Carolina?": ["Catamounts", "Lady Catamounts"]},
    {"What is the nickname for Western Connecticut State?": ["Colonials"]},
    {"What is the nickname for Western Illinois?": ["Fighting Leathernecks", "Westerwinds"]},
    {"What is the nickname for Western Kentucky University?": ["Hilltoppers"]},
    {"What is the nickname for Western Michigan University?": ["Broncos"]},
    {"What is the nickname for Western Nebraska Community College?": ["Cougars"]},
    {"What is the nickname for Western Oregon University?": ["Wolves"]},
    {"What is the nickname for Western Texas College?": ["Westerners", "Lady Westerners"]},
    {"What is the nickname for Western Washington University?": ["Vikings"]},
    {"What is the nickname for Westmont College?": ["Warriors"]},
    {"What is the nickname for Wheaton College Illinois?": ["Thunder"]},
    {"What is the nickname for Wheaton College Massachusetts?": ["Lyons"]},
    {"What is the nickname for Wheeling Jesuit?": ["Cardinals"]},
    {"What is the nickname for Whitman College?": ["Missionaries"]},
    {"What is the nickname for Whittier College?": ["Poets"]},
    {"What is the nickname for Wichita State University?": ["Shockers"]},
    {"What is the nickname for Widener University?": ["Pride"]},
    {"What is the nickname for Wiley College?": ["Wildcats"]},
    {"What is the nickname for Wilkes University?": ["Colonels"]},
    {"What is the nickname for College of William and Mary?": ["Tribe"]},
    {"What is the nickname for William Carey University?": ["Crusaders"]},
    {"What is the nickname for William Jewell College?": ["Cardinals"]},
    {"What is the nickname for William Paterson University?": ["Pioneers"]},
    {"What is the nickname for William Penn University?": ["Statesmen", "Lady Statesmen"]},
    {"What is the nickname for William Smith College?": ["Herons"]},
    {"What is the nickname for William Woods University?": ["Owls"]},
    {"What is the nickname for Williams?": ["Ephs"]},
    {"What is the nickname for Williston State College?": ["Tetons"]},
    {"What is the nickname for Wilmington College Ohio?": ["Fighting Quakers"]},
    {"What is the nickname for Winona State University?": ["Warriors"]},
    {"What is the nickname for Winston-Salem State University?": ["Rams", "Lady Rams"]},
    {"What is the nickname for Winthrop University?": ["Eagles"]},
    {"What is the nickname for Wisconsin–Eau Claire?": ["Blugolds"]},
    {"What is the nickname for Wisconsin–Green Bay?": ["Phoenix"]},
    {"What is the nickname for Wisconsin–La Crosse?": ["Eagles"]},
    {"What is the nickname for Wisconsin-Madison?": ["Badgers"]},
    {"What is the nickname for Wisconsin–Marathon County?": ["Huskies"]},
    {"What is the nickname for Wisconsin–Marshfield Wood County?": ["Marauders"]},
    {"What is the nickname for Wisconsin–Milwaukee?": ["Panthers"]},
    {"What is the nickname for Wisconsin-Oshkosh?": ["Titans"]},
    {"What is the nickname for Wisconsin–Parkside?": ["Rangers"]},
    {"What is the nickname for Wisconsin–Platteville?": ["Pioneers"]},
    {"What is the nickname for Wisconsin-Richland?": ["Roadrunners"]},
    {"What is the nickname for Wisconsin–River Falls?": ["Falcons"]},
    {"What is the nickname for Wisconsin-Rock County?": ["Rattlesnakes"]},
    {"What is the nickname for Wisconsin-Sheboygan?": ["Wombats"]},
    {"What is the nickname for Wisconsin–Steven's Point?": ["Pointers"]},
    {"What is the nickname for Wisconsin–Stout?": ["Blue Devils"]},
    {"What is the nickname for Wisconsin–Superior?": ["Yellowjackets"]},
    {"What is the nickname for Wisconsin–-Whitewater?": ["Warhawks"]},
    {"What is the nickname for Wittenberg?": ["Tigers"]},
    {"What is the nickname for Wofford?": ["Terrier"]},
    {"What is the nickname for Wooster?": ["Fighting Scots"]},
    {"What is the nickname for Worcester Polytechnic Institute?": ["Engineers"]},
    {"What is the nickname for Worcester State College?": ["Lancers"]},
    {"What is the nickname for Wright State?": ["Raiders"]},
    {"What is the nickname for Wyoming?": ["Cowboys", "Cowgirls"]},
    {"What is the nickname for Xavier University (Cincinnati)?": ["Musketeers"]},
    {"What is the nickname for Yale University?": ["Bulldogs", "Elis"]},
    {"What is the nickname for Yeshiva University?": ["Maccabees"]},
    {"What is the nickname for York College of Pennsylvania?": ["Spartans"]},
    {"What is the nickname for Youngstown State University?": ["Penguins"]}
]


def lambda_handler(event, context):
    """
    Route the incoming request based on type (LaunchRequest, IntentRequest, etc).
    The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID
    to prevent someone else from configuring a skill that sends requests
    to this function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """Called when the session starts."""
    print("on_session_started requestId=" +
          session_started_request['requestId'] + ", sessionId=" +
          session['sessionId'])


def on_launch(launch_request, session):
    """Called when the user launches the skill without specifying what they want."""
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """Called when the user specifies an intent for this skill."""
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # handle yes/no intent after the user has been prompted
    if session.get('attributes', {}).get('user_prompted_to_continue'):
        del session['attributes']['user_prompted_to_continue']
        if intent_name == 'AMAZON.NoIntent':
            return handle_finish_session_request(intent, session)
        elif intent_name == "AMAZON.YesIntent":
            return handle_repeat_request(intent, session)

    # Dispatch to your skill's intent handlers
    if intent_name == "AnswerIntent":
        return handle_answer_request(intent, session)
    elif intent_name == "AnswerOnlyIntent":
        return handle_answer_request(intent, session)
    elif intent_name == "AMAZON.YesIntent":
        return handle_answer_request(intent, session)
    elif intent_name == "AMAZON.NoIntent":
        return handle_answer_request(intent, session)
    elif intent_name == "AMAZON.StartOverIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.RepeatIntent":
        return handle_repeat_request(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return handle_get_help_request(intent, session)
    elif intent_name == "AMAZON.StopIntent":
        return handle_finish_session_request(intent, session)
    elif intent_name == "AMAZON.CancelIntent":
        return handle_finish_session_request(intent, session)
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """
    Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Functions that control the skill's behavior -------------


def get_welcome_response():
    """If we wanted to initialize the session to have some attributes we could add those here."""
    intro = ("Let's play {}. ".format(SKILL_NAME) +
             "I will ask you {} questions. ".format(GAME_LENGTH) +
             "Try to get as many right as you can. Just say the answer. Let's begin. ")
    should_end_session = False
    game_questions = populate_game_questions()
    starting_index = 0

    #spoken_question = QUESTIONS[game_questions[starting_index]].keys()[0]
    spoken_question = list(QUESTIONS[game_questions[starting_index]].keys())[0]

    speech_output = intro + spoken_question
    attributes = {"speech_output": speech_output,
                  "reprompt_text": spoken_question,
                  "current_questions_index": starting_index,
                  "questions": game_questions,
                  "score": 0,
    #              "correct_answers": QUESTIONS[game_questions[starting_index]].values()[0]
                  "correct_answers": list(QUESTIONS[game_questions[starting_index]].values())[0]
                  }

    return build_response(attributes, build_speechlet_response(
        SKILL_NAME, speech_output, spoken_question, should_end_session))


def populate_game_questions():
    game_questions = []
    index_list = []
    index = len(QUESTIONS)

    if GAME_LENGTH > index:
        raise ValueError("Invalid Game Length")

    for i in range(0, index):
        index_list.append(i)

    # Pick GAME_LENGTH random questions from the list to ask the user,
    # make sure there are no repeats
    for j in range(0, GAME_LENGTH):
        rand = int(math.floor(random.random() * index))
        index -= 1

        temp = index_list[index]
        index_list[index] = index_list[rand]
        index_list[rand] = temp
        game_questions.append(index_list[index])

    return game_questions


def handle_answer_request(intent, session):
    attributes = {}
    should_end_session = False
    answer = intent['slots'].get('Answer', {}).get('value')
    user_gave_up = intent['name']

    if 'attributes' in session.keys() and 'questions' not in session['attributes'].keys():
        # If the user responded with an answer but there is no game
        # in progress ask the user if they want to start a new game.
        # Set a flag to track that we've prompted the user.
        attributes['user_prompted_to_continue'] = True
        speech_output = "There is no game in progress. " \
                        "Do you want to start a new game?"
        reprompt_text = speech_output
        return build_response(attributes, build_speechlet_response(SKILL_NAME,
                              speech_output, reprompt_text, should_end_session))
    elif not answer and user_gave_up == "DontKnowIntent":
        # If the user provided answer isn't a number > 0 and < ANSWER_COUNT,
        # return an error message to the user. Remember to guide the user
        # into providing correct values.
        reprompt = session['attributes']['speech_output']
        speech_output = "Your answer must be a known element " + reprompt
        return build_response(
            session['attributes'],
            build_speechlet_response(
                SKILL_NAME, speech_output, reprompt_text, should_end_session
            ))
    else:
        game_questions = session['attributes']['questions']
        current_score = session['attributes']['score']
        current_questions_index = session['attributes']['current_questions_index']
        correct_answers = session['attributes']['correct_answers']

        speech_output_analysis = None
        if answer and answer.lower() in map(string.lower, correct_answers):
            current_score += 1
            speech_output_analysis = "correct. "
        else:
            if user_gave_up != "DontKnowIntent":
                speech_output_analysis = "wrong. "
            speech_output_analysis = (speech_output_analysis +
                                      "The correct answer is " +
                                      correct_answers[0])

        # if current_questions_index is 4, we've reached 5 questions
        # (zero-indexed) and can exit the game session
        if current_questions_index == GAME_LENGTH - 1:
            speech_output = "" if intent['name'] == "DontKnowIntent" else "That answer is "
            speech_output = (speech_output + speech_output_analysis +
                             "You got {} out of {} correct. ".format(current_score, GAME_LENGTH) +
                             "Thank you for playing {} with Alexa!".format(SKILL_NAME))
            reprompt_text = None
            should_end_session = True
            return build_response(
                session['attributes'],
                build_speechlet_response(
                    SKILL_NAME, speech_output, reprompt_text, should_end_session
                ))
        else:
            current_questions_index += 1
            spoken_question = QUESTIONS[game_questions[current_questions_index]].keys()[0]
            reprompt_text = spoken_question

            speech_output = "" if user_gave_up == "DontKnowIntent" else "That answer is "
            speech_output = (speech_output + speech_output_analysis +
                             "Your score is " +
                             str(current_score) + '. ' + reprompt_text)
            attributes = {"speech_output": speech_output,
                          "reprompt_text": reprompt_text,
                          "current_questions_index": current_questions_index,
                          "questions": game_questions,
                          "score": current_score,
                          "correct_answers": QUESTIONS[game_questions[current_questions_index]].values()[0]  # noqa
                          }

            return build_response(attributes,
                                  build_speechlet_response(SKILL_NAME, speech_output, reprompt_text,
                                                           should_end_session))


def handle_repeat_request(intent, session):
    """
    Repeat the previous speech_output and reprompt_text from the session['attributes'].
    If available, else start a new game session.
    """
    if 'attributes' not in session or 'speech_output' not in session['attributes']:
        return get_welcome_response()
    else:
        attributes = session['attributes']
        speech_output = attributes['speech_output']
        reprompt_text = attributes['reprompt_text']
        should_end_session = False
        return build_response(
            attributes,
            build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session)
        )


def handle_get_help_request(intent, session):
    attributes = {}
    speech_output = ("You can begin a game by saying start a new game, or, "
                     "you can say exit... What can I help you with?")
    reprompt_text = "What can I help you with?"
    should_end_session = False
    return build_response(
        attributes,
        build_speechlet_response(SKILL_NAME, speech_output, reprompt_text, should_end_session)
    )


def handle_finish_session_request(intent, session):
    """End the session with a message if the user wants to quit the game."""
    attributes = session['attributes']
    reprompt_text = None
    speech_output = "Thanks for playing {}!".format(SKILL_NAME)
    should_end_session = True
    return build_response(
        attributes,
        build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session)
    )


def is_answer_slot_valid(intent):
    if 'Answer' in intent['slots'].keys() and 'value' in intent['slots']['Answer'].keys():
        return True
    else:
        return False


# --------------- Helpers that build all of the responses -----------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_speechlet_response_without_card(output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response': speechlet_response
    }
