# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 16:41:34 2016

@author: harry
"""

import yaml

nsw_dict = {
    'IDR404' : {'location' : 'Captains_Flat', 'range' : 64 , 'refresh_rate' : 6},
    'IDR403' : {'location' : 'Captains_Flat', 'range' : 128, 'refresh_rate' : 6},
    'IDR402' : {'location' : 'Captains_Flat', 'range' : 256, 'refresh_rate' : 6},
    'IDR401' : {'location' : 'Captains_Flat', 'range' : 512, 'refresh_rate' : 6},
    'IDR044' : {'location' : 'Lemon_tree', 'range' : 64 , 'refresh_rate' : 6},
    'IDR043' : {'location' : 'Lemon_tree', 'range' : 128, 'refresh_rate' : 6},
    'IDR042' : {'location' : 'Lemon_tree', 'range' : 256, 'refresh_rate' : 6},
    'IDR041' : {'location' : 'Lemon_tree', 'range' : 512, 'refresh_rate' : 6},
    'IDR694' : {'location' : 'Namoi', 'range' : 64 , 'refresh_rate' : 10},
    'IDR693' : {'location' : 'Namoi', 'range' : 128, 'refresh_rate' : 10},
    'IDR692' : {'location' : 'Namoi', 'range' : 256, 'refresh_rate' : 10},
    'IDR691' : {'location' : 'Namoi', 'range' : 512, 'refresh_rate' : 10},
    'IDR623' : {'location' : 'Norfolk_Island', 'range' : 128, 'refresh_rate' : 10},
    'IDR622' : {'location' : 'Norfolk_Island', 'range' : 256, 'refresh_rate' : 10},
    'IDR621' : {'location' : 'Norfolk_Island', 'range' : 512, 'refresh_rate' : 10},
    'IDR283' : {'location' : 'Grafton', 'range' : 128, 'refresh_rate' : 10},
    'IDR282' : {'location' : 'Grafton', 'range' : 256, 'refresh_rate' : 10},
    'IDR281' : {'location' : 'Grafton', 'range' : 512, 'refresh_rate' : 10},
    'IDR533' : {'location' : 'Moree', 'range' : 128, 'refresh_rate' : 10},
    'IDR532' : {'location' : 'Moree', 'range' : 256, 'refresh_rate' : 10},
    'IDR531' : {'location' : 'Moree', 'range' : 512, 'refresh_rate' : 10},
    'IDR714' : {'location' : 'Terrey_Hills', 'range' : 64 , 'refresh_rate' : 6},
    'IDR713' : {'location' : 'Terrey_Hills', 'range' : 128, 'refresh_rate' : 6},
    'IDR712' : {'location' : 'Terrey_Hills', 'range' : 256, 'refresh_rate' : 6},
    'IDR711' : {'location' : 'Terrey_Hills', 'range' : 512, 'refresh_rate' : 6},
    'IDR553' : {'location' : 'Wagga_Wagga', 'range' : 128, 'refresh_rate' : 10},
    'IDR552' : {'location' : 'Wagga_Wagga', 'range' : 256, 'refresh_rate' : 10},
    'IDR551' : {'location' : 'Wagga_Wagga', 'range' : 512, 'refresh_rate' : 10},
    'IDR034' : {'location' : 'Wollongong', 'range' : 64 , 'refresh_rate' : 6},
    'IDR033' : {'location' : 'Wollongong', 'range' : 128, 'refresh_rate' : 6},
    'IDR032' : {'location' : 'Wollongong', 'range' : 256, 'refresh_rate' : 6},
    'IDR031' : {'location' : 'Wollongong', 'range' : 512, 'refresh_rate' : 6}
    }

qld_dict = {
    'IDR664' : {'location' : 'Brisbane', 'range' : 64 , 'refresh_rate' : 6},
    'IDR663' : {'location' : 'Brisbane', 'range' : 128, 'refresh_rate' : 6},
    'IDR662' : {'location' : 'Brisbane', 'range' : 256, 'refresh_rate' : 6},
    'IDR661' : {'location' : 'Brisbane', 'range' : 512, 'refresh_rate' : 6},
    'IDR243' : {'location' : 'Bowen', 'range' : 128, 'refresh_rate' : 10},
    'IDR242' : {'location' : 'Bowen', 'range' : 256, 'refresh_rate' : 10},
    'IDR241' : {'location' : 'Bowen', 'range' : 512, 'refresh_rate' : 10},
    'IDR194' : {'location' : 'Cairns', 'range' : 64 , 'refresh_rate' : 6},
    'IDR193' : {'location' : 'Cairns', 'range' : 128, 'refresh_rate' : 6},
    'IDR192' : {'location' : 'Cairns', 'range' : 256, 'refresh_rate' : 6},
    'IDR191' : {'location' : 'Cairns', 'range' : 512, 'refresh_rate' : 6},
    'IDR724' : {'location' : 'Emerald', 'range' : 64 , 'refresh_rate' : 10},
    'IDR723' : {'location' : 'Emerald', 'range' : 128, 'refresh_rate' : 10},
    'IDR722' : {'location' : 'Emerald', 'range' : 256, 'refresh_rate' : 10},
    'IDR721' : {'location' : 'Emerald', 'range' : 512, 'refresh_rate' : 10},
    'IDR233' : {'location' : 'Gladstone', 'range' : 128, 'refresh_rate' : 10},
    'IDR232' : {'location' : 'Gladstone', 'range' : 256, 'refresh_rate' : 10},
    'IDR231' : {'location' : 'Gladstone', 'range' : 512, 'refresh_rate' : 10},
    'IDR083' : {'location' : 'Gympie', 'range' : 128, 'refresh_rate' : 10},
    'IDR082' : {'location' : 'Gympie', 'range' : 256, 'refresh_rate' : 10},
    'IDR081' : {'location' : 'Gympie', 'range' : 512, 'refresh_rate' : 10},
    'IDR563' : {'location' : 'Longreach', 'range' : 128, 'refresh_rate' : 10},
    'IDR562' : {'location' : 'Longreach', 'range' : 256, 'refresh_rate' : 10},
    'IDR561' : {'location' : 'Longreach', 'range' : 512, 'refresh_rate' : 10},
    'IDR223' : {'location' : 'Mackay', 'range' : 128, 'refresh_rate' : 10},
    'IDR222' : {'location' : 'Mackay', 'range' : 256, 'refresh_rate' : 10},
    'IDR221' : {'location' : 'Mackay', 'range' : 512, 'refresh_rate' : 10},
    'IDR503' : {'location' : 'Marburg', 'range' : 128, 'refresh_rate' : 10},
    'IDR502' : {'location' : 'Marburg', 'range' : 256, 'refresh_rate' : 10},
    'IDR501' : {'location' : 'Marburg', 'range' : 512, 'refresh_rate' : 10},
    'IDR363' : {'location' : 'Mornington_Island', 'range' : 128, 'refresh_rate' : 10},
    'IDR362' : {'location' : 'Mornington_Island', 'range' : 256, 'refresh_rate' : 10},
    'IDR361' : {'location' : 'Mornington_Island', 'range' : 512, 'refresh_rate' : 10},
    'IDR754' : {'location' : 'Mt_Isa', 'range' : 64 , 'refresh_rate' : 6},
    'IDR753' : {'location' : 'Mt_Isa', 'range' : 128, 'refresh_rate' : 6},
    'IDR752' : {'location' : 'Mt_Isa', 'range' : 256, 'refresh_rate' : 6},
    'IDR751' : {'location' : 'Mt_Isa', 'range' : 512, 'refresh_rate' : 6},
    'IDR734' : {'location' : 'Townsville', 'range' : 64 , 'refresh_rate' : 10},
    'IDR733' : {'location' : 'Townsville', 'range' : 128, 'refresh_rate' : 10},
    'IDR732' : {'location' : 'Townsville', 'range' : 256, 'refresh_rate' : 10},
    'IDR731' : {'location' : 'Townsville', 'range' : 512, 'refresh_rate' : 10},
    'IDR673' : {'location' : 'Warrego', 'range' : 128, 'refresh_rate' : 10},
    'IDR672' : {'location' : 'Warrego', 'range' : 256, 'refresh_rate' : 10},
    'IDR671' : {'location' : 'Warrego', 'range' : 512, 'refresh_rate' : 10},
    'IDR784' : {'location' : 'Weipa', 'range' : 64 , 'refresh_rate' : 6},
    'IDR783' : {'location' : 'Weipa', 'range' : 128, 'refresh_rate' : 6},
    'IDR782' : {'location' : 'Weipa', 'range' : 256, 'refresh_rate' : 6},
    'IDR781' : {'location' : 'Weipa', 'range' : 512, 'refresh_rate' : 6},
    'IDR413' : {'location' : 'Willis_Island', 'range' : 128, 'refresh_rate' : 10},
    'IDR412' : {'location' : 'Willis_Island', 'range' : 256, 'refresh_rate' : 10},
    'IDR411' : {'location' : 'Willis_Island', 'range' : 512, 'refresh_rate' : 10},
    }

nt_dict = {
    'IDR253' : {'location' : 'Alice_Springs', 'range' : 128, 'refresh_rate' : 10},
    'IDR252' : {'location' : 'Alice_Springs', 'range' : 256, 'refresh_rate' : 10},
    'IDR251' : {'location' : 'Alice_Springs', 'range' : 512, 'refresh_rate' : 10},
    'IDR634' : {'location' : 'Darwin', 'range' : 64 , 'refresh_rate' : 10},
    'IDR633' : {'location' : 'Darwin', 'range' : 128, 'refresh_rate' : 10},
    'IDR632' : {'location' : 'Darwin', 'range' : 256, 'refresh_rate' : 10},
    'IDR631' : {'location' : 'Darwin', 'range' : 512, 'refresh_rate' : 10},
    'IDR093' : {'location' : 'Gove', 'range' : 128, 'refresh_rate' : 10},
    'IDR092' : {'location' : 'Gove', 'range' : 256, 'refresh_rate' : 10},
    'IDR091' : {'location' : 'Gove', 'range' : 512, 'refresh_rate' : 10},
    'IDR423' : {'location' : 'Katherine', 'range' : 128, 'refresh_rate' : 10},
    'IDR422' : {'location' : 'Katherine', 'range' : 256, 'refresh_rate' : 10},
    'IDR421' : {'location' : 'Katherine', 'range' : 512, 'refresh_rate' : 10},
    'IDR774' : {'location' : 'Warruwi', 'range' : 64 , 'refresh_rate' : 6},
    'IDR773' : {'location' : 'Warruwi', 'range' : 128, 'refresh_rate' : 6},
    'IDR772' : {'location' : 'Warruwi', 'range' : 256, 'refresh_rate' : 6},
    'IDR771' : {'location' : 'Warruwi', 'range' : 512, 'refresh_rate' : 6}
    }

sa_dict = {
    'IDR644' : {'location' : 'Adelaide', 'range' : 64 , 'refresh_rate' : 10},
    'IDR643' : {'location' : 'Adelaide', 'range' : 128, 'refresh_rate' : 10},
    'IDR642' : {'location' : 'Adelaide', 'range' : 256, 'refresh_rate' : 10},
    'IDR641' : {'location' : 'Adelaide', 'range' : 512, 'refresh_rate' : 10},
    'IDR333' : {'location' : 'Ceduna', 'range' : 128, 'refresh_rate' : 10},
    'IDR332' : {'location' : 'Ceduna', 'range' : 256, 'refresh_rate' : 10},
    'IDR331' : {'location' : 'Ceduna', 'range' : 512, 'refresh_rate' : 10},
    'IDR143' : {'location' : 'Mt_Gambier', 'range' : 128, 'refresh_rate' : 10},
    'IDR142' : {'location' : 'Mt_Gambier', 'range' : 256, 'refresh_rate' : 10},
    'IDR141' : {'location' : 'Mt_Gambier', 'range' : 512, 'refresh_rate' : 10},
    'IDR463' : {'location' : 'Sellicks_Hill', 'range' : 128, 'refresh_rate' : 10},
    'IDR462' : {'location' : 'Sellicks_Hill', 'range' : 256, 'refresh_rate' : 10},
    'IDR461' : {'location' : 'Sellicks_Hill', 'range' : 512, 'refresh_rate' : 10},
    'IDR273' : {'location' : 'Woomera', 'range' : 128, 'refresh_rate' : 10},
    'IDR272' : {'location' : 'Woomera', 'range' : 256, 'refresh_rate' : 10},
    'IDR271' : {'location' : 'Woomera', 'range' : 512, 'refresh_rate' : 10},
    }

wa_dict = {
    'IDR313' : {'location' : 'Albany', 'range' : 128, 'refresh_rate' : 10},
    'IDR312' : {'location' : 'Albany', 'range' : 256, 'refresh_rate' : 10},
    'IDR311' : {'location' : 'Albany', 'range' : 512, 'refresh_rate' : 10},
    'IDR173' : {'location' : 'Broome', 'range' : 128, 'refresh_rate' : 10},
    'IDR172' : {'location' : 'Broome', 'range' : 256, 'refresh_rate' : 10},
    'IDR171' : {'location' : 'Broome', 'range' : 512, 'refresh_rate' : 10},
    'IDR053' : {'location' : 'Carnarvon', 'range' : 128, 'refresh_rate' : 10},
    'IDR052' : {'location' : 'Carnarvon', 'range' : 256, 'refresh_rate' : 10},
    'IDR051' : {'location' : 'Carnarvon', 'range' : 512, 'refresh_rate' : 10},
    'IDR153' : {'location' : 'Dampier', 'range' : 128, 'refresh_rate' : 10},
    'IDR152' : {'location' : 'Dampier', 'range' : 256, 'refresh_rate' : 10},
    'IDR151' : {'location' : 'Dampier', 'range' : 512, 'refresh_rate' : 10},
    'IDR323' : {'location' : 'Esperance', 'range' : 128, 'refresh_rate' : 10},
    'IDR322' : {'location' : 'Esperance', 'range' : 256, 'refresh_rate' : 10},
    'IDR321' : {'location' : 'Esperance', 'range' : 512, 'refresh_rate' : 10},
    'IDR063' : {'location' : 'Geraldton', 'range' : 128, 'refresh_rate' : 10},
    'IDR062' : {'location' : 'Geraldton', 'range' : 256, 'refresh_rate' : 10},
    'IDR061' : {'location' : 'Geraldton', 'range' : 512, 'refresh_rate' : 10},
    'IDR443' : {'location' : 'Giles', 'range' : 128, 'refresh_rate' : 10},
    'IDR442' : {'location' : 'Giles', 'range' : 256, 'refresh_rate' : 10},
    'IDR441' : {'location' : 'Giles', 'range' : 512, 'refresh_rate' : 10},
    'IDR393' : {'location' : 'Halls_Creek', 'range' : 128, 'refresh_rate' : 10},
    'IDR392' : {'location' : 'Halls_Creek', 'range' : 256, 'refresh_rate' : 10},
    'IDR391' : {'location' : 'Halls_Creek', 'range' : 512, 'refresh_rate' : 10},
    'IDR483' : {'location' : 'Kalgoorlie', 'range' : 128, 'refresh_rate' : 10},
    'IDR482' : {'location' : 'Kalgoorlie', 'range' : 256, 'refresh_rate' : 10},
    'IDR481' : {'location' : 'Kalgoorlie', 'range' : 512, 'refresh_rate' : 10},
    'IDR293' : {'location' : 'Learmonth', 'range' : 128, 'refresh_rate' : 10},
    'IDR292' : {'location' : 'Learmonth', 'range' : 256, 'refresh_rate' : 10},
    'IDR291' : {'location' : 'Learmonth', 'range' : 512, 'refresh_rate' : 10},
    'IDR704' : {'location' : 'Perth', 'range' : 64 , 'refresh_rate' : 10},
    'IDR703' : {'location' : 'Perth', 'range' : 128, 'refresh_rate' : 10},
    'IDR702' : {'location' : 'Perth', 'range' : 256, 'refresh_rate' : 10},
    'IDR701' : {'location' : 'Perth', 'range' : 512, 'refresh_rate' : 10},
    'IDR163' : {'location' : 'Port_Headland', 'range' : 128, 'refresh_rate' : 10},
    'IDR162' : {'location' : 'Port_Headland', 'range' : 256, 'refresh_rate' : 10},
    'IDR161' : {'location' : 'Port_Headland', 'range' : 512, 'refresh_rate' : 10},
    'IDR073' : {'location' : 'Wyndham', 'range' : 128, 'refresh_rate' : 10},
    'IDR072' : {'location' : 'Wyndham', 'range' : 256, 'refresh_rate' : 10},
    'IDR071' : {'location' : 'Wyndham', 'range' : 512, 'refresh_rate' : 10},
    }

vic_dict = {
    'IDR683' : {'location' : 'Bairnsdale', 'range' : 128, 'refresh_rate' : 10},
    'IDR682' : {'location' : 'Bairnsdale', 'range' : 256, 'refresh_rate' : 10},
    'IDR681' : {'location' : 'Bairnsdale', 'range' : 512, 'refresh_rate' : 10},
    'IDR024' : {'location' : 'Melbourne', 'range' : 64 , 'refresh_rate' : 6},
    'IDR023' : {'location' : 'Melbourne', 'range' : 128, 'refresh_rate' : 6},
    'IDR022' : {'location' : 'Melbourne', 'range' : 256, 'refresh_rate' : 6},
    'IDR021' : {'location' : 'Melbourne', 'range' : 512, 'refresh_rate' : 6},
    'IDR303' : {'location' : 'Mildura', 'range' : 128, 'refresh_rate' : 10},
    'IDR302' : {'location' : 'Mildura', 'range' : 256, 'refresh_rate' : 10},
    'IDR301' : {'location' : 'Mildura', 'range' : 512, 'refresh_rate' : 10},
    'IDR494' : {'location' : 'Yarrawonga', 'range' : 64 , 'refresh_rate' : 10},
    'IDR493' : {'location' : 'Yarrawonga', 'range' : 128, 'refresh_rate' : 10},
    'IDR492' : {'location' : 'Yarrawonga', 'range' : 256, 'refresh_rate' : 10},
    'IDR491' : {'location' : 'Yarrawonga', 'range' : 512, 'refresh_rate' : 10}
    }

tas_dict = {
    'IDR764' : {'location' : 'Hobart', 'range' : 64 , 'refresh_rate' : 6},
    'IDR763' : {'location' : 'Hobart', 'range' : 128, 'refresh_rate' : 6},
    'IDR762' : {'location' : 'Hobart', 'range' : 256, 'refresh_rate' : 6},
    'IDR761' : {'location' : 'Hobart', 'range' : 512, 'refresh_rate' : 6},
    'IDR523' : {'location' : 'West_Takone', 'range' : 128, 'refresh_rate' : 10},
    'IDR522' : {'location' : 'West_Takone', 'range' : 256, 'refresh_rate' : 10},
    'IDR521' : {'location' : 'West_Takone', 'range' : 512, 'refresh_rate' : 10}
    }

# combine the dictionaries
IDtoDetails_dict = {}
IDtoDetails_dict.update(nsw_dict)
IDtoDetails_dict.update(qld_dict)
IDtoDetails_dict.update(nt_dict)
IDtoDetails_dict.update(wa_dict)
IDtoDetails_dict.update(vic_dict)
IDtoDetails_dict.update(tas_dict)
IDtoDetails_dict.update(sa_dict)

with open('radar_config.yml', 'w') as fd:
    yaml.dump(IDtoDetails_dict, fd)
