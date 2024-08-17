import json

# Sample JSON data
data = [
  {
    "issueNumber": "20240722011260",
    "number": "2",
    "colour": "red",
    "premium": "50392"
  },
  {
    "issueNumber": "20240722011259",
    "number": "9",
    "colour": "green",
    "premium": "92619"
  },
  {
    "issueNumber": "20240722011258",
    "number": "2",
    "colour": "red",
    "premium": "26632"
  },
  {
    "issueNumber": "20240722011257",
    "number": "1",
    "colour": "green",
    "premium": "38471"
  },
  {
    "issueNumber": "20240722011256",
    "number": "1",
    "colour": "green",
    "premium": "22201"
  },
  {
    "issueNumber": "20240722011255",
    "number": "5",
    "colour": "green,violet",
    "premium": "21545"
  },
  {
    "issueNumber": "20240722011254",
    "number": "1",
    "colour": "green",
    "premium": "37071"
  },
  {
    "issueNumber": "20240722011253",
    "number": "9",
    "colour": "green",
    "premium": "53489"
  },
  {
    "issueNumber": "20240722011252",
    "number": "4",
    "colour": "red",
    "premium": "38944"
  },
  {
    "issueNumber": "20240722011251",
    "number": "0",
    "colour": "red,violet",
    "premium": "92080"
  },
  {
    "issueNumber": "20240722011250",
    "number": "3",
    "colour": "green",
    "premium": "56823"
  },
  {
    "issueNumber": "20240722011249",
    "number": "9",
    "colour": "green",
    "premium": "72059"
  },
  {
    "issueNumber": "20240722011248",
    "number": "7",
    "colour": "green",
    "premium": "28227"
  },
  {
    "issueNumber": "20240722011247",
    "number": "3",
    "colour": "green",
    "premium": "79633"
  },
  {
    "issueNumber": "20240722011246",
    "number": "6",
    "colour": "red",
    "premium": "23216"
  },
  {
    "issueNumber": "20240722011245",
    "number": "1",
    "colour": "green",
    "premium": "60701"
  },
  {
    "issueNumber": "20240722011244",
    "number": "3",
    "colour": "green",
    "premium": "88633"
  },
  {
    "issueNumber": "20240722011243",
    "number": "1",
    "colour": "green",
    "premium": "77041"
  },
  {
    "issueNumber": "20240722011242",
    "number": "4",
    "colour": "red",
    "premium": "12714"
  },
  {
    "issueNumber": "20240722011241",
    "number": "0",
    "colour": "red,violet",
    "premium": "77810"
  },
  {
    "issueNumber": "20240722011240",
    "number": "0",
    "colour": "red,violet",
    "premium": "54640"
  },
  {
    "issueNumber": "20240722011239",
    "number": "7",
    "colour": "green",
    "premium": "93707"
  },
  {
    "issueNumber": "20240722011238",
    "number": "0",
    "colour": "red,violet",
    "premium": "47150"
  },
  {
    "issueNumber": "20240722011237",
    "number": "8",
    "colour": "red",
    "premium": "64458"
  },
  {
    "issueNumber": "20240722011236",
    "number": "6",
    "colour": "red",
    "premium": "48106"
  },
  {
    "issueNumber": "20240722011235",
    "number": "3",
    "colour": "green",
    "premium": "58913"
  },
  {
    "issueNumber": "20240722011234",
    "number": "8",
    "colour": "red",
    "premium": "76428"
  },
  {
    "issueNumber": "20240722011233",
    "number": "1",
    "colour": "green",
    "premium": "27071"
  },
  {
    "issueNumber": "20240722011232",
    "number": "0",
    "colour": "red,violet",
    "premium": "32050"
  },
  {
    "issueNumber": "20240722011231",
    "number": "0",
    "colour": "red,violet",
    "premium": "79610"
  },
  {
    "issueNumber": "20240722011230",
    "number": "3",
    "colour": "green",
    "premium": "75673"
  },
  {
    "issueNumber": "20240722011229",
    "number": "4",
    "colour": "red",
    "premium": "68644"
  },
  {
    "issueNumber": "20240722011228",
    "number": "7",
    "colour": "green",
    "premium": "87207"
  },
  {
    "issueNumber": "20240722011227",
    "number": "3",
    "colour": "green",
    "premium": "91193"
  },
  {
    "issueNumber": "20240722011226",
    "number": "1",
    "colour": "green",
    "premium": "63761"
  },
  {
    "issueNumber": "20240722011225",
    "number": "7",
    "colour": "green",
    "premium": "88637"
  },
  {
    "issueNumber": "20240722011224",
    "number": "0",
    "colour": "red,violet",
    "premium": "59270"
  },
  {
    "issueNumber": "20240722011223",
    "number": "3",
    "colour": "green",
    "premium": "81813"
  },
  {
    "issueNumber": "20240722011222",
    "number": "1",
    "colour": "green",
    "premium": "64471"
  },
  {
    "issueNumber": "20240722011221",
    "number": "4",
    "colour": "red",
    "premium": "46294"
  },
  {
    "issueNumber": "20240722011220",
    "number": "1",
    "colour": "green",
    "premium": "63361"
  },
  {
    "issueNumber": "20240722011219",
    "number": "2",
    "colour": "red",
    "premium": "72012"
  },
  {
    "issueNumber": "20240722011218",
    "number": "7",
    "colour": "green",
    "premium": "81607"
  },
  {
    "issueNumber": "20240722011217",
    "number": "5",
    "colour": "green,violet",
    "premium": "54695"
  },
  {
    "issueNumber": "20240722011216",
    "number": "8",
    "colour": "red",
    "premium": "76788"
  },
  {
    "issueNumber": "20240722011215",
    "number": "0",
    "colour": "red,violet",
    "premium": "69680"
  },
  {
    "issueNumber": "20240722011214",
    "number": "8",
    "colour": "red",
    "premium": "20278"
  },
  {
    "issueNumber": "20240722011213",
    "number": "4",
    "colour": "red",
    "premium": "98574"
  },
  {
    "issueNumber": "20240722011212",
    "number": "4",
    "colour": "red",
    "premium": "14834"
  },
  {
    "issueNumber": "20240722011211",
    "number": "6",
    "colour": "red",
    "premium": "17886"
  },
  {
    "issueNumber": "20240722011210",
    "number": "6",
    "colour": "red",
    "premium": "73986"
  },
  {
    "issueNumber": "20240722011209",
    "number": "7",
    "colour": "green",
    "premium": "79717"
  },
  {
    "issueNumber": "20240722011208",
    "number": "8",
    "colour": "red",
    "premium": "68098"
  },
  {
    "issueNumber": "20240722011207",
    "number": "2",
    "colour": "red",
    "premium": "25732"
  },
  {
    "issueNumber": "20240722011206",
    "number": "4",
    "colour": "red",
    "premium": "87694"
  },
  {
    "issueNumber": "20240722011205",
    "number": "0",
    "colour": "red,violet",
    "premium": "40770"
  },
  {
    "issueNumber": "20240722011204",
    "number": "3",
    "colour": "green",
    "premium": "64523"
  },
  {
    "issueNumber": "20240722011203",
    "number": "4",
    "colour": "red",
    "premium": "95574"
  },
  {
    "issueNumber": "20240722011202",
    "number": "7",
    "colour": "green",
    "premium": "84537"
  },
  {
    "issueNumber": "20240722011201",
    "number": "3",
    "colour": "green",
    "premium": "85233"
  },
  {
    "issueNumber": "20240722011200",
    "number": "2",
    "colour": "red",
    "premium": "51602"
  },
  {
    "issueNumber": "20240722011199",
    "number": "1",
    "colour": "green",
    "premium": "57981"
  },
  {
    "issueNumber": "20240722011198",
    "number": "7",
    "colour": "green",
    "premium": "44237"
  },
  {
    "issueNumber": "20240722011197",
    "number": "5",
    "colour": "green,violet",
    "premium": "72565"
  },
  {
    "issueNumber": "20240722011196",
    "number": "1",
    "colour": "green",
    "premium": "29801"
  },
  {
    "issueNumber": "20240722011195",
    "number": "9",
    "colour": "green",
    "premium": "46119"
  },
  {
    "issueNumber": "20240722011194",
    "number": "4",
    "colour": "red",
    "premium": "27584"
  },
  {
    "issueNumber": "20240722011193",
    "number": "7",
    "colour": "green",
    "premium": "26487"
  },
  {
    "issueNumber": "20240722011192",
    "number": "3",
    "colour": "green",
    "premium": "30753"
  },
  {
    "issueNumber": "20240722011191",
    "number": "1",
    "colour": "green",
    "premium": "87421"
  },
  {
    "issueNumber": "20240722011190",
    "number": "1",
    "colour": "green",
    "premium": "47001"
  },
  {
    "issueNumber": "20240722011189",
    "number": "6",
    "colour": "red",
    "premium": "68326"
  },
  {
    "issueNumber": "20240722011188",
    "number": "2",
    "colour": "red",
    "premium": "10622"
  },
  {
    "issueNumber": "20240722011187",
    "number": "5",
    "colour": "green,violet",
    "premium": "97935"
  },
  {
    "issueNumber": "20240722011186",
    "number": "4",
    "colour": "red",
    "premium": "89644"
  },
  {
    "issueNumber": "20240722011185",
    "number": "3",
    "colour": "green",
    "premium": "17223"
  },
  {
    "issueNumber": "20240722011184",
    "number": "8",
    "colour": "red",
    "premium": "38518"
  },
  {
    "issueNumber": "20240722011183",
    "number": "7",
    "colour": "green",
    "premium": "95367"
  },
  {
    "issueNumber": "20240722011182",
    "number": "0",
    "colour": "red,violet",
    "premium": "25850"
  },
  {
    "issueNumber": "20240722011181",
    "number": "9",
    "colour": "green",
    "premium": "40599"
  },
  {
    "issueNumber": "20240722011180",
    "number": "0",
    "colour": "red,violet",
    "premium": "26460"
  },
  {
    "issueNumber": "20240722011179",
    "number": "7",
    "colour": "green",
    "premium": "33227"
  },
  {
    "issueNumber": "20240722011178",
    "number": "1",
    "colour": "green",
    "premium": "85531"
  },
  {
    "issueNumber": "20240722011177",
    "number": "6",
    "colour": "red",
    "premium": "48246"
  },
  {
    "issueNumber": "20240722011176",
    "number": "1",
    "colour": "green",
    "premium": "37321"
  },
  {
    "issueNumber": "20240722011175",
    "number": "9",
    "colour": "green",
    "premium": "55319"
  },
  {
    "issueNumber": "20240722011174",
    "number": "8",
    "colour": "red",
    "premium": "41818"
  },
  {
    "issueNumber": "20240722011173",
    "number": "1",
    "colour": "green",
    "premium": "99131"
  },
  {
    "issueNumber": "20240722011172",
    "number": "2",
    "colour": "red",
    "premium": "39542"
  },
  {
    "issueNumber": "20240722011171",
    "number": "0",
    "colour": "red,violet",
    "premium": "72400"
  },
  {
    "issueNumber": "20240722011170",
    "number": "9",
    "colour": "green",
    "premium": "20539"
  },
  {
    "issueNumber": "20240722011169",
    "number": "3",
    "colour": "green",
    "premium": "30003"
  },
  {
    "issueNumber": "20240722011168",
    "number": "0",
    "colour": "red,violet",
    "premium": "95240"
  },
  {
    "issueNumber": "20240722011167",
    "number": "5",
    "colour": "green,violet",
    "premium": "21835"
  },
  {
    "issueNumber": "20240722011166",
    "number": "9",
    "colour": "green",
    "premium": "48079"
  },
  {
    "issueNumber": "20240722011165",
    "number": "5",
    "colour": "green,violet",
    "premium": "26025"
  },
  {
    "issueNumber": "20240722011164",
    "number": "2",
    "colour": "red",
    "premium": "87092"
  },
  {
    "issueNumber": "20240722011163",
    "number": "2",
    "colour": "red",
    "premium": "44082"
  },
  {
    "issueNumber": "20240722011162",
    "number": "0",
    "colour": "red,violet",
    "premium": "97700"
  },
  {
    "issueNumber": "20240722011161",
    "number": "9",
    "colour": "green",
    "premium": "53869"
  },
  {
    "issueNumber": "20240722011160",
    "number": "7",
    "colour": "green",
    "premium": "48607"
  },
  {
    "issueNumber": "20240722011159",
    "number": "6",
    "colour": "red",
    "premium": "31946"
  },
  {
    "issueNumber": "20240722011158",
    "number": "7",
    "colour": "green",
    "premium": "57467"
  },
  {
    "issueNumber": "20240722011157",
    "number": "9",
    "colour": "green",
    "premium": "85189"
  },
  {
    "issueNumber": "20240722011156",
    "number": "2",
    "colour": "red",
    "premium": "62762"
  },
  {
    "issueNumber": "20240722011155",
    "number": "6",
    "colour": "red",
    "premium": "39076"
  },
  {
    "issueNumber": "20240722011154",
    "number": "1",
    "colour": "green",
    "premium": "77931"
  },
  {
    "issueNumber": "20240722011153",
    "number": "6",
    "colour": "red",
    "premium": "71376"
  },
  {
    "issueNumber": "20240722011152",
    "number": "7",
    "colour": "green",
    "premium": "84647"
  },
  {
    "issueNumber": "20240722011151",
    "number": "6",
    "colour": "red",
    "premium": "25256"
  },
  {
    "issueNumber": "20240722011150",
    "number": "4",
    "colour": "red",
    "premium": "56074"
  },
  {
    "issueNumber": "20240722011149",
    "number": "1",
    "colour": "green",
    "premium": "45301"
  },
  {
    "issueNumber": "20240722011148",
    "number": "1",
    "colour": "green",
    "premium": "42581"
  },
  {
    "issueNumber": "20240722011147",
    "number": "2",
    "colour": "red",
    "premium": "58802"
  },
  {
    "issueNumber": "20240722011146",
    "number": "7",
    "colour": "green",
    "premium": "44687"
  },
  {
    "issueNumber": "20240722011145",
    "number": "5",
    "colour": "green,violet",
    "premium": "68165"
  },
  {
    "issueNumber": "20240722011144",
    "number": "6",
    "colour": "red",
    "premium": "85246"
  },
  {
    "issueNumber": "20240722011143",
    "number": "0",
    "colour": "red,violet",
    "premium": "93160"
  },
  {
    "issueNumber": "20240722011142",
    "number": "5",
    "colour": "green,violet",
    "premium": "79255"
  },
  {
    "issueNumber": "20240722011141",
    "number": "1",
    "colour": "green",
    "premium": "36051"
  },
  {
    "issueNumber": "20240722011140",
    "number": "6",
    "colour": "red",
    "premium": "97796"
  },
  {
    "issueNumber": "20240722011139",
    "number": "0",
    "colour": "red,violet",
    "premium": "61210"
  },
  {
    "issueNumber": "20240722011138",
    "number": "0",
    "colour": "red,violet",
    "premium": "35080"
  },
  {
    "issueNumber": "20240722011137",
    "number": "5",
    "colour": "green,violet",
    "premium": "81435"
  },
  {
    "issueNumber": "20240722011136",
    "number": "6",
    "colour": "red",
    "premium": "66696"
  },
  {
    "issueNumber": "20240722011135",
    "number": "6",
    "colour": "red",
    "premium": "18406"
  },
  {
    "issueNumber": "20240722011134",
    "number": "5",
    "colour": "green,violet",
    "premium": "57445"
  },
  {
    "issueNumber": "20240722011133",
    "number": "3",
    "colour": "green",
    "premium": "40963"
  },
  {
    "issueNumber": "20240722011132",
    "number": "6",
    "colour": "red",
    "premium": "74046"
  },
  {
    "issueNumber": "20240722011131",
    "number": "4",
    "colour": "red",
    "premium": "15414"
  },
  {
    "issueNumber": "20240722011130",
    "number": "3",
    "colour": "green",
    "premium": "91583"
  },
  {
    "issueNumber": "20240722011129",
    "number": "5",
    "colour": "green,violet",
    "premium": "48375"
  },
  {
    "issueNumber": "20240722011128",
    "number": "3",
    "colour": "green",
    "premium": "31283"
  },
  {
    "issueNumber": "20240722011127",
    "number": "7",
    "colour": "green",
    "premium": "34307"
  },
  {
    "issueNumber": "20240722011126",
    "number": "4",
    "colour": "red",
    "premium": "17114"
  },
  {
    "issueNumber": "20240722011125",
    "number": "7",
    "colour": "green",
    "premium": "28307"
  },
  {
    "issueNumber": "20240722011124",
    "number": "1",
    "colour": "green",
    "premium": "39661"
  },
  {
    "issueNumber": "20240722011123",
    "number": "1",
    "colour": "green",
    "premium": "12571"
  },
  {
    "issueNumber": "20240722011122",
    "number": "6",
    "colour": "red",
    "premium": "81716"
  },
  {
    "issueNumber": "20240722011121",
    "number": "4",
    "colour": "red",
    "premium": "22504"
  },
  {
    "issueNumber": "20240722011120",
    "number": "8",
    "colour": "red",
    "premium": "17488"
  },
  {
    "issueNumber": "20240722011119",
    "number": "7",
    "colour": "green",
    "premium": "35447"
  },
  {
    "issueNumber": "20240722011118",
    "number": "6",
    "colour": "red",
    "premium": "75396"
  },
  {
    "issueNumber": "20240722011117",
    "number": "6",
    "colour": "red",
    "premium": "19896"
  },
  {
    "issueNumber": "20240722011116",
    "number": "9",
    "colour": "green",
    "premium": "38009"
  },
  {
    "issueNumber": "20240722011115",
    "number": "3",
    "colour": "green",
    "premium": "21513"
  },
  {
    "issueNumber": "20240722011114",
    "number": "7",
    "colour": "green",
    "premium": "63137"
  },
  {
    "issueNumber": "20240722011113",
    "number": "8",
    "colour": "red",
    "premium": "19548"
  },
  {
    "issueNumber": "20240722011112",
    "number": "1",
    "colour": "green",
    "premium": "74031"
  },
  {
    "issueNumber": "20240722011111",
    "number": "3",
    "colour": "green",
    "premium": "92823"
  },
  {
    "issueNumber": "20240722011110",
    "number": "1",
    "colour": "green",
    "premium": "94841"
  },
  {
    "issueNumber": "20240722011109",
    "number": "9",
    "colour": "green",
    "premium": "14699"
  },
  {
    "issueNumber": "20240722011108",
    "number": "9",
    "colour": "green",
    "premium": "63309"
  },
  {
    "issueNumber": "20240722011107",
    "number": "0",
    "colour": "red,violet",
    "premium": "73380"
  },
  {
    "issueNumber": "20240722011106",
    "number": "7",
    "colour": "green",
    "premium": "55097"
  },
  {
    "issueNumber": "20240722011105",
    "number": "4",
    "colour": "red",
    "premium": "89044"
  },
  {
    "issueNumber": "20240722011104",
    "number": "2",
    "colour": "red",
    "premium": "75772"
  },
  {
    "issueNumber": "20240722011103",
    "number": "6",
    "colour": "red",
    "premium": "10376"
  },
  {
    "issueNumber": "20240722011102",
    "number": "2",
    "colour": "red",
    "premium": "93732"
  },
  {
    "issueNumber": "20240722011101",
    "number": "8",
    "colour": "red",
    "premium": "92058"
  },
  {
    "issueNumber": "20240722011100",
    "number": "4",
    "colour": "red",
    "premium": "36574"
  },
  {
    "issueNumber": "20240722011099",
    "number": "7",
    "colour": "green",
    "premium": "76107"
  },
  {
    "issueNumber": "20240722011098",
    "number": "4",
    "colour": "red",
    "premium": "60334"
  },
  {
    "issueNumber": "20240722011097",
    "number": "5",
    "colour": "green,violet",
    "premium": "85485"
  },
  {
    "issueNumber": "20240722011096",
    "number": "8",
    "colour": "red",
    "premium": "37538"
  },
  {
    "issueNumber": "20240722011095",
    "number": "3",
    "colour": "green",
    "premium": "94383"
  },
  {
    "issueNumber": "20240722011094",
    "number": "0",
    "colour": "red,violet",
    "premium": "82760"
  },
  {
    "issueNumber": "20240722011093",
    "number": "3",
    "colour": "green",
    "premium": "89933"
  },
  {
    "issueNumber": "20240722011092",
    "number": "7",
    "colour": "green",
    "premium": "11477"
  },
  {
    "issueNumber": "20240722011091",
    "number": "3",
    "colour": "green",
    "premium": "14993"
  },
  {
    "issueNumber": "20240722011090",
    "number": "5",
    "colour": "green,violet",
    "premium": "83605"
  },
  {
    "issueNumber": "20240722011089",
    "number": "3",
    "colour": "green",
    "premium": "42823"
  },
  {
    "issueNumber": "20240722011088",
    "number": "3",
    "colour": "green",
    "premium": "54113"
  },
  {
    "issueNumber": "20240722011087",
    "number": "4",
    "colour": "red",
    "premium": "61524"
  },
  {
    "issueNumber": "20240722011086",
    "number": "0",
    "colour": "red,violet",
    "premium": "12480"
  },
  {
    "issueNumber": "20240722011085",
    "number": "2",
    "colour": "red",
    "premium": "40492"
  },
  {
    "issueNumber": "20240722011084",
    "number": "5",
    "colour": "green,violet",
    "premium": "12265"
  },
  {
    "issueNumber": "20240722011083",
    "number": "5",
    "colour": "green,violet",
    "premium": "29025"
  },
  {
    "issueNumber": "20240722011082",
    "number": "0",
    "colour": "red,violet",
    "premium": "35420"
  },
  {
    "issueNumber": "20240722011081",
    "number": "5",
    "colour": "green,violet",
    "premium": "46135"
  },
  {
    "issueNumber": "20240722011080",
    "number": "0",
    "colour": "red,violet",
    "premium": "74900"
  },
  {
    "issueNumber": "20240722011079",
    "number": "2",
    "colour": "red",
    "premium": "30222"
  },
  {
    "issueNumber": "20240722011078",
    "number": "3",
    "colour": "green",
    "premium": "11853"
  },
  {
    "issueNumber": "20240722011077",
    "number": "6",
    "colour": "red",
    "premium": "20156"
  },
  {
    "issueNumber": "20240722011076",
    "number": "5",
    "colour": "green,violet",
    "premium": "56855"
  },
  {
    "issueNumber": "20240722011075",
    "number": "8",
    "colour": "red",
    "premium": "20068"
  },
  {
    "issueNumber": "20240722011074",
    "number": "9",
    "colour": "green",
    "premium": "29479"
  },
  {
    "issueNumber": "20240722011073",
    "number": "3",
    "colour": "green",
    "premium": "32843"
  },
  {
    "issueNumber": "20240722011072",
    "number": "6",
    "colour": "red",
    "premium": "23986"
  },
  {
    "issueNumber": "20240722011071",
    "number": "8",
    "colour": "red",
    "premium": "80048"
  },
  {
    "issueNumber": "20240722011070",
    "number": "2",
    "colour": "red",
    "premium": "64032"
  },
  {
    "issueNumber": "20240722011069",
    "number": "4",
    "colour": "red",
    "premium": "14984"
  },
  {
    "issueNumber": "20240722011068",
    "number": "1",
    "colour": "green",
    "premium": "88671"
  },
  {
    "issueNumber": "20240722011067",
    "number": "5",
    "colour": "green,violet",
    "premium": "15195"
  },
  {
    "issueNumber": "20240722011066",
    "number": "0",
    "colour": "red,violet",
    "premium": "17340"
  },
  {
    "issueNumber": "20240722011065",
    "number": "3",
    "colour": "green",
    "premium": "75253"
  },
  {
    "issueNumber": "20240722011064",
    "number": "6",
    "colour": "red",
    "premium": "81296"
  },
  {
    "issueNumber": "20240722011063",
    "number": "7",
    "colour": "green",
    "premium": "59607"
  },
  {
    "issueNumber": "20240722011062",
    "number": "5",
    "colour": "green,violet",
    "premium": "42225"
  },
  {
    "issueNumber": "20240722011061",
    "number": "8",
    "colour": "red",
    "premium": "28858"
  },
  {
    "issueNumber": "20240722011060",
    "number": "3",
    "colour": "green",
    "premium": "73633"
  },
  {
    "issueNumber": "20240722011059",
    "number": "3",
    "colour": "green",
    "premium": "84133"
  },
  {
    "issueNumber": "20240722011058",
    "number": "2",
    "colour": "red",
    "premium": "35792"
  },
  {
    "issueNumber": "20240722011057",
    "number": "4",
    "colour": "red",
    "premium": "25344"
  },
  {
    "issueNumber": "20240722011056",
    "number": "0",
    "colour": "red,violet",
    "premium": "79970"
  },
  {
    "issueNumber": "20240722011055",
    "number": "4",
    "colour": "red",
    "premium": "34234"
  },
  {
    "issueNumber": "20240722011054",
    "number": "4",
    "colour": "red",
    "premium": "44864"
  },
  {
    "issueNumber": "20240722011053",
    "number": "6",
    "colour": "red",
    "premium": "34276"
  },
  {
    "issueNumber": "20240722011052",
    "number": "2",
    "colour": "red",
    "premium": "60412"
  },
  {
    "issueNumber": "20240722011051",
    "number": "5",
    "colour": "green,violet",
    "premium": "30265"
  },
  {
    "issueNumber": "20240722011050",
    "number": "2",
    "colour": "red",
    "premium": "14552"
  },
  {
    "issueNumber": "20240722011049",
    "number": "3",
    "colour": "green",
    "premium": "47243"
  },
  {
    "issueNumber": "20240722011048",
    "number": "9",
    "colour": "green",
    "premium": "82969"
  },
  {
    "issueNumber": "20240722011047",
    "number": "9",
    "colour": "green",
    "premium": "41489"
  },
  {
    "issueNumber": "20240722011046",
    "number": "1",
    "colour": "green",
    "premium": "50541"
  },
  {
    "issueNumber": "20240722011045",
    "number": "3",
    "colour": "green",
    "premium": "39113"
  },
  {
    "issueNumber": "20240722011044",
    "number": "6",
    "colour": "red",
    "premium": "56736"
  },
  {
    "issueNumber": "20240722011043",
    "number": "6",
    "colour": "red",
    "premium": "63926"
  },
  {
    "issueNumber": "20240722011042",
    "number": "4",
    "colour": "red",
    "premium": "46914"
  },
  {
    "issueNumber": "20240722011041",
    "number": "3",
    "colour": "green",
    "premium": "26433"
  },
  {
    "issueNumber": "20240722011040",
    "number": "4",
    "colour": "red",
    "premium": "56214"
  },
  {
    "issueNumber": "20240722011039",
    "number": "1",
    "colour": "green",
    "premium": "59231"
  },
  {
    "issueNumber": "20240722011038",
    "number": "6",
    "colour": "red",
    "premium": "13826"
  },
  {
    "issueNumber": "20240722011037",
    "number": "5",
    "colour": "green,violet",
    "premium": "60685"
  },
  {
    "issueNumber": "20240722011036",
    "number": "4",
    "colour": "red",
    "premium": "75634"
  },
  {
    "issueNumber": "20240722011035",
    "number": "9",
    "colour": "green",
    "premium": "13119"
  },
  {
    "issueNumber": "20240722011034",
    "number": "9",
    "colour": "green",
    "premium": "21889"
  },
  {
    "issueNumber": "20240722011033",
    "number": "7",
    "colour": "green",
    "premium": "94667"
  },
  {
    "issueNumber": "20240722011032",
    "number": "0",
    "colour": "red,violet",
    "premium": "64840"
  },
  {
    "issueNumber": "20240722011031",
    "number": "3",
    "colour": "green",
    "premium": "44593"
  },
  {
    "issueNumber": "20240722011030",
    "number": "1",
    "colour": "green",
    "premium": "86471"
  },
  {
    "issueNumber": "20240722011029",
    "number": "3",
    "colour": "green",
    "premium": "69063"
  },
  {
    "issueNumber": "20240722011028",
    "number": "2",
    "colour": "red",
    "premium": "11012"
  },
  {
    "issueNumber": "20240722011027",
    "number": "7",
    "colour": "green",
    "premium": "56177"
  },
  {
    "issueNumber": "20240722011026",
    "number": "4",
    "colour": "red",
    "premium": "67454"
  },
  {
    "issueNumber": "20240722011025",
    "number": "8",
    "colour": "red",
    "premium": "70888"
  },
  {
    "issueNumber": "20240722011024",
    "number": "9",
    "colour": "green",
    "premium": "66849"
  },
  {
    "issueNumber": "20240722011023",
    "number": "1",
    "colour": "green",
    "premium": "15391"
  },
  {
    "issueNumber": "20240722011022",
    "number": "0",
    "colour": "red,violet",
    "premium": "53330"
  },
  {
    "issueNumber": "20240722011021",
    "number": "9",
    "colour": "green",
    "premium": "12169"
  },
  {
    "issueNumber": "20240722011020",
    "number": "3",
    "colour": "green",
    "premium": "75693"
  },
  {
    "issueNumber": "20240722011019",
    "number": "4",
    "colour": "red",
    "premium": "10874"
  },
  {
    "issueNumber": "20240722011018",
    "number": "4",
    "colour": "red",
    "premium": "19514"
  },
  {
    "issueNumber": "20240722011017",
    "number": "0",
    "colour": "red,violet",
    "premium": "54290"
  },
  {
    "issueNumber": "20240722011016",
    "number": "8",
    "colour": "red",
    "premium": "28888"
  },
  {
    "issueNumber": "20240722011015",
    "number": "3",
    "colour": "green",
    "premium": "90643"
  },
  {
    "issueNumber": "20240722011014",
    "number": "7",
    "colour": "green",
    "premium": "37267"
  },
  {
    "issueNumber": "20240722011013",
    "number": "8",
    "colour": "red",
    "premium": "49008"
  },
  {
    "issueNumber": "20240722011012",
    "number": "2",
    "colour": "red",
    "premium": "95652"
  },
  {
    "issueNumber": "20240722011011",
    "number": "9",
    "colour": "green",
    "premium": "75979"
  },
  {
    "issueNumber": "20240722011010",
    "number": "8",
    "colour": "red",
    "premium": "25968"
  },
  {
    "issueNumber": "20240722011009",
    "number": "6",
    "colour": "red",
    "premium": "22116"
  },
  {
    "issueNumber": "20240722011008",
    "number": "2",
    "colour": "red",
    "premium": "46152"
  },
  {
    "issueNumber": "20240722011007",
    "number": "7",
    "colour": "green",
    "premium": "61397"
  },
  {
    "issueNumber": "20240722011006",
    "number": "3",
    "colour": "green",
    "premium": "40423"
  },
  {
    "issueNumber": "20240722011005",
    "number": "2",
    "colour": "red",
    "premium": "23872"
  },
  {
    "issueNumber": "20240722011004",
    "number": "9",
    "colour": "green",
    "premium": "40819"
  },
  {
    "issueNumber": "20240722011003",
    "number": "1",
    "colour": "green",
    "premium": "45001"
  },
  {
    "issueNumber": "20240722011002",
    "number": "9",
    "colour": "green",
    "premium": "38009"
  },
  {
    "issueNumber": "20240722011001",
    "number": "5",
    "colour": "green,violet",
    "premium": "54575"
  },
  {
    "issueNumber": "20240722011000",
    "number": "9",
    "colour": "green",
    "premium": "60569"
  },
  {
    "issueNumber": "20240722010999",
    "number": "6",
    "colour": "red",
    "premium": "99116"
  },
  {
    "issueNumber": "20240722010998",
    "number": "9",
    "colour": "green",
    "premium": "61879"
  },
  {
    "issueNumber": "20240722010997",
    "number": "2",
    "colour": "red",
    "premium": "62172"
  },
  {
    "issueNumber": "20240722010996",
    "number": "9",
    "colour": "green",
    "premium": "36939"
  },
  {
    "issueNumber": "20240722010995",
    "number": "9",
    "colour": "green",
    "premium": "85859"
  },
  {
    "issueNumber": "20240722010994",
    "number": "4",
    "colour": "red",
    "premium": "44354"
  },
  {
    "issueNumber": "20240722010993",
    "number": "2",
    "colour": "red",
    "premium": "18852"
  },
  {
    "issueNumber": "20240722010992",
    "number": "0",
    "colour": "red,violet",
    "premium": "74400"
  },
  {
    "issueNumber": "20240722010991",
    "number": "1",
    "colour": "green",
    "premium": "63641"
  },
  {
    "issueNumber": "20240722010990",
    "number": "2",
    "colour": "red",
    "premium": "14442"
  },
  {
    "issueNumber": "20240722010989",
    "number": "8",
    "colour": "red",
    "premium": "98298"
  },
  {
    "issueNumber": "20240722010988",
    "number": "3",
    "colour": "green",
    "premium": "11423"
  },
  {
    "issueNumber": "20240722010987",
    "number": "6",
    "colour": "red",
    "premium": "78956"
  },
  {
    "issueNumber": "20240722010986",
    "number": "4",
    "colour": "red",
    "premium": "54854"
  },
  {
    "issueNumber": "20240722010985",
    "number": "1",
    "colour": "green",
    "premium": "66331"
  },
  {
    "issueNumber": "20240722010984",
    "number": "5",
    "colour": "green,violet",
    "premium": "82795"
  },
  {
    "issueNumber": "20240722010983",
    "number": "6",
    "colour": "red",
    "premium": "43236"
  },
  {
    "issueNumber": "20240722010982",
    "number": "7",
    "colour": "green",
    "premium": "31517"
  },
  {
    "issueNumber": "20240722010981",
    "number": "4",
    "colour": "red",
    "premium": "91244"
  },
  {
    "issueNumber": "20240722010980",
    "number": "3",
    "colour": "green",
    "premium": "68853"
  },
  {
    "issueNumber": "20240722010979",
    "number": "8",
    "colour": "red",
    "premium": "10948"
  },
  {
    "issueNumber": "20240722010978",
    "number": "6",
    "colour": "red",
    "premium": "74526"
  },
  {
    "issueNumber": "20240722010977",
    "number": "5",
    "colour": "green,violet",
    "premium": "11385"
  },
  {
    "issueNumber": "20240722010976",
    "number": "0",
    "colour": "red,violet",
    "premium": "55430"
  },
  {
    "issueNumber": "20240722010975",
    "number": "7",
    "colour": "green",
    "premium": "27297"
  },
  {
    "issueNumber": "20240722010974",
    "number": "5",
    "colour": "green,violet",
    "premium": "88405"
  },
  {
    "issueNumber": "20240722010973",
    "number": "7",
    "colour": "green",
    "premium": "26707"
  },
  {
    "issueNumber": "20240722010972",
    "number": "5",
    "colour": "green,violet",
    "premium": "30175"
  },
  {
    "issueNumber": "20240722010971",
    "number": "5",
    "colour": "green,violet",
    "premium": "64015"
  },
  {
    "issueNumber": "20240722010970",
    "number": "4",
    "colour": "red",
    "premium": "86194"
  },
  {
    "issueNumber": "20240722010969",
    "number": "9",
    "colour": "green",
    "premium": "37489"
  },
  {
    "issueNumber": "20240722010968",
    "number": "8",
    "colour": "red",
    "premium": "45368"
  },
  {
    "issueNumber": "20240722010967",
    "number": "2",
    "colour": "red",
    "premium": "40722"
  },
  {
    "issueNumber": "20240722010966",
    "number": "9",
    "colour": "green",
    "premium": "44759"
  },
  {
    "issueNumber": "20240722010965",
    "number": "7",
    "colour": "green",
    "premium": "38037"
  },
  {
    "issueNumber": "20240722010964",
    "number": "7",
    "colour": "green",
    "premium": "34277"
  },
  {
    "issueNumber": "20240722010963",
    "number": "9",
    "colour": "green",
    "premium": "38159"
  },
  {
    "issueNumber": "20240722010962",
    "number": "9",
    "colour": "green",
    "premium": "96189"
  },
  {
    "issueNumber": "20240722010961",
    "number": "6",
    "colour": "red",
    "premium": "59566"
  },
  {
    "issueNumber": "20240722010960",
    "number": "4",
    "colour": "red",
    "premium": "13414"
  },
  {
    "issueNumber": "20240722010959",
    "number": "5",
    "colour": "green,violet",
    "premium": "31705"
  },
  {
    "issueNumber": "20240722010958",
    "number": "2",
    "colour": "red",
    "premium": "99382"
  },
  {
    "issueNumber": "20240722010957",
    "number": "3",
    "colour": "green",
    "premium": "70393"
  },
  {
    "issueNumber": "20240722010956",
    "number": "1",
    "colour": "green",
    "premium": "64951"
  },
  {
    "issueNumber": "20240722010955",
    "number": "1",
    "colour": "green",
    "premium": "21431"
  },
  {
    "issueNumber": "20240722010954",
    "number": "1",
    "colour": "green",
    "premium": "19681"
  },
  {
    "issueNumber": "20240722010953",
    "number": "0",
    "colour": "red,violet",
    "premium": "81250"
  },
  {
    "issueNumber": "20240722010952",
    "number": "6",
    "colour": "red",
    "premium": "47946"
  },
  {
    "issueNumber": "20240722010951",
    "number": "2",
    "colour": "red",
    "premium": "36052"
  },
  {
    "issueNumber": "20240722010950",
    "number": "6",
    "colour": "red",
    "premium": "82286"
  },
  {
    "issueNumber": "20240722010949",
    "number": "4",
    "colour": "red",
    "premium": "60424"
  },
  {
    "issueNumber": "20240722010948",
    "number": "7",
    "colour": "green",
    "premium": "54007"
  },
  {
    "issueNumber": "20240722010947",
    "number": "8",
    "colour": "red",
    "premium": "82838"
  },
  {
    "issueNumber": "20240722010946",
    "number": "8",
    "colour": "red",
    "premium": "66018"
  },
  {
    "issueNumber": "20240722010945",
    "number": "9",
    "colour": "green",
    "premium": "97949"
  },
  {
    "issueNumber": "20240722010944",
    "number": "1",
    "colour": "green",
    "premium": "87001"
  },
  {
    "issueNumber": "20240722010943",
    "number": "0",
    "colour": "red,violet",
    "premium": "69190"
  },
  {
    "issueNumber": "20240722010942",
    "number": "6",
    "colour": "red",
    "premium": "69196"
  },
  {
    "issueNumber": "20240722010941",
    "number": "9",
    "colour": "green",
    "premium": "30399"
  },
  {
    "issueNumber": "20240722010940",
    "number": "6",
    "colour": "red",
    "premium": "78426"
  },
  {
    "issueNumber": "20240722010939",
    "number": "2",
    "colour": "red",
    "premium": "82902"
  },
  {
    "issueNumber": "20240722010938",
    "number": "3",
    "colour": "green",
    "premium": "50863"
  },
  {
    "issueNumber": "20240722010937",
    "number": "8",
    "colour": "red",
    "premium": "36238"
  },
  {
    "issueNumber": "20240722010936",
    "number": "6",
    "colour": "red",
    "premium": "98876"
  },
  {
    "issueNumber": "20240722010935",
    "number": "6",
    "colour": "red",
    "premium": "90216"
  },
  {
    "issueNumber": "20240722010934",
    "number": "0",
    "colour": "red,violet",
    "premium": "59300"
  },
  {
    "issueNumber": "20240722010933",
    "number": "1",
    "colour": "green",
    "premium": "59811"
  },
  {
    "issueNumber": "20240722010932",
    "number": "8",
    "colour": "red",
    "premium": "49188"
  },
  {
    "issueNumber": "20240722010931",
    "number": "8",
    "colour": "red",
    "premium": "75258"
  },
  {
    "issueNumber": "20240722010930",
    "number": "0",
    "colour": "red,violet",
    "premium": "13190"
  },
  {
    "issueNumber": "20240722010929",
    "number": "3",
    "colour": "green",
    "premium": "64003"
  },
  {
    "issueNumber": "20240722010928",
    "number": "2",
    "colour": "red",
    "premium": "77172"
  },
  {
    "issueNumber": "20240722010927",
    "number": "8",
    "colour": "red",
    "premium": "96978"
  },
  {
    "issueNumber": "20240722010926",
    "number": "6",
    "colour": "red",
    "premium": "33636"
  },
  {
    "issueNumber": "20240722010925",
    "number": "7",
    "colour": "green",
    "premium": "88217"
  },
  {
    "issueNumber": "20240722010924",
    "number": "2",
    "colour": "red",
    "premium": "69482"
  },
  {
    "issueNumber": "20240722010923",
    "number": "8",
    "colour": "red",
    "premium": "85378"
  },
  {
    "issueNumber": "20240722010922",
    "number": "0",
    "colour": "red,violet",
    "premium": "53560"
  },
  {
    "issueNumber": "20240722010921",
    "number": "9",
    "colour": "green",
    "premium": "12139"
  },
  {
    "issueNumber": "20240722010920",
    "number": "9",
    "colour": "green",
    "premium": "34089"
  },
  {
    "issueNumber": "20240722010919",
    "number": "8",
    "colour": "red",
    "premium": "74128"
  },
  {
    "issueNumber": "20240722010918",
    "number": "6",
    "colour": "red",
    "premium": "74986"
  },
  {
    "issueNumber": "20240722010917",
    "number": "4",
    "colour": "red",
    "premium": "68524"
  },
  {
    "issueNumber": "20240722010916",
    "number": "8",
    "colour": "red",
    "premium": "78378"
  },
  {
    "issueNumber": "20240722010915",
    "number": "0",
    "colour": "red,violet",
    "premium": "99450"
  },
  {
    "issueNumber": "20240722010914",
    "number": "5",
    "colour": "green,violet",
    "premium": "36765"
  },
  {
    "issueNumber": "20240722010913",
    "number": "7",
    "colour": "green",
    "premium": "77657"
  },
  {
    "issueNumber": "20240722010912",
    "number": "0",
    "colour": "red,violet",
    "premium": "54570"
  },
  {
    "issueNumber": "20240722010911",
    "number": "0",
    "colour": "red,violet",
    "premium": "58110"
  },
  {
    "issueNumber": "20240722010910",
    "number": "7",
    "colour": "green",
    "premium": "42817"
  },
  {
    "issueNumber": "20240722010909",
    "number": "3",
    "colour": "green",
    "premium": "90453"
  },
  {
    "issueNumber": "20240722010908",
    "number": "6",
    "colour": "red",
    "premium": "70026"
  },
  {
    "issueNumber": "20240722010907",
    "number": "7",
    "colour": "green",
    "premium": "96527"
  },
  {
    "issueNumber": "20240722010906",
    "number": "1",
    "colour": "green",
    "premium": "29361"
  },
  {
    "issueNumber": "20240722010905",
    "number": "0",
    "colour": "red,violet",
    "premium": "92400"
  },
  {
    "issueNumber": "20240722010904",
    "number": "0",
    "colour": "red,violet",
    "premium": "38940"
  },
  {
    "issueNumber": "20240722010903",
    "number": "7",
    "colour": "green",
    "premium": "98557"
  },
  {
    "issueNumber": "20240722010902",
    "number": "7",
    "colour": "green",
    "premium": "89967"
  },
  {
    "issueNumber": "20240722010901",
    "number": "6",
    "colour": "red",
    "premium": "13286"
  },
  {
    "issueNumber": "20240722010900",
    "number": "6",
    "colour": "red",
    "premium": "37076"
  },
  {
    "issueNumber": "20240722010899",
    "number": "8",
    "colour": "red",
    "premium": "34728"
  },
  {
    "issueNumber": "20240722010898",
    "number": "6",
    "colour": "red",
    "premium": "57846"
  },
  {
    "issueNumber": "20240722010897",
    "number": "4",
    "colour": "red",
    "premium": "29414"
  },
  {
    "issueNumber": "20240722010896",
    "number": "4",
    "colour": "red",
    "premium": "51854"
  },
  {
    "issueNumber": "20240722010895",
    "number": "9",
    "colour": "green",
    "premium": "71479"
  },
  {
    "issueNumber": "20240722010894",
    "number": "1",
    "colour": "green",
    "premium": "24521"
  },
  {
    "issueNumber": "20240722010893",
    "number": "0",
    "colour": "red,violet",
    "premium": "47110"
  },
  {
    "issueNumber": "20240722010892",
    "number": "0",
    "colour": "red,violet",
    "premium": "35750"
  },
  {
    "issueNumber": "20240722010891",
    "number": "0",
    "colour": "red,violet",
    "premium": "48060"
  },
  {
    "issueNumber": "20240722010890",
    "number": "3",
    "colour": "green",
    "premium": "47613"
  },
  {
    "issueNumber": "20240722010889",
    "number": "6",
    "colour": "red",
    "premium": "41786"
  },
  {
    "issueNumber": "20240722010888",
    "number": "0",
    "colour": "red,violet",
    "premium": "97490"
  },
  {
    "issueNumber": "20240722010887",
    "number": "9",
    "colour": "green",
    "premium": "90889"
  },
  {
    "issueNumber": "20240722010886",
    "number": "4",
    "colour": "red",
    "premium": "13484"
  },
  {
    "issueNumber": "20240722010885",
    "number": "7",
    "colour": "green",
    "premium": "84497"
  },
  {
    "issueNumber": "20240722010884",
    "number": "3",
    "colour": "green",
    "premium": "56493"
  },
  {
    "issueNumber": "20240722010883",
    "number": "8",
    "colour": "red",
    "premium": "11498"
  },
  {
    "issueNumber": "20240722010882",
    "number": "4",
    "colour": "red",
    "premium": "75794"
  },
  {
    "issueNumber": "20240722010881",
    "number": "8",
    "colour": "red",
    "premium": "88768"
  },
  {
    "issueNumber": "20240722010880",
    "number": "6",
    "colour": "red",
    "premium": "36226"
  },
  {
    "issueNumber": "20240722010879",
    "number": "9",
    "colour": "green",
    "premium": "43779"
  },
  {
    "issueNumber": "20240722010878",
    "number": "2",
    "colour": "red",
    "premium": "31702"
  },
  {
    "issueNumber": "20240722010877",
    "number": "0",
    "colour": "red,violet",
    "premium": "56480"
  },
  {
    "issueNumber": "20240722010876",
    "number": "5",
    "colour": "green,violet",
    "premium": "88935"
  },
  {
    "issueNumber": "20240722010875",
    "number": "4",
    "colour": "red",
    "premium": "55834"
  },
  {
    "issueNumber": "20240722010874",
    "number": "9",
    "colour": "green",
    "premium": "79229"
  },
  {
    "issueNumber": "20240722010873",
    "number": "6",
    "colour": "red",
    "premium": "41446"
  },
  {
    "issueNumber": "20240722010872",
    "number": "7",
    "colour": "green",
    "premium": "70357"
  },
  {
    "issueNumber": "20240722010871",
    "number": "0",
    "colour": "red,violet",
    "premium": "58140"
  },
  {
    "issueNumber": "20240722010870",
    "number": "2",
    "colour": "red",
    "premium": "82602"
  },
  {
    "issueNumber": "20240722010869",
    "number": "2",
    "colour": "red",
    "premium": "68042"
  },
  {
    "issueNumber": "20240722010868",
    "number": "6",
    "colour": "red",
    "premium": "93576"
  },
  {
    "issueNumber": "20240722010867",
    "number": "8",
    "colour": "red",
    "premium": "86778"
  },
  {
    "issueNumber": "20240722010866",
    "number": "5",
    "colour": "green,violet",
    "premium": "41335"
  },
  {
    "issueNumber": "20240722010865",
    "number": "7",
    "colour": "green",
    "premium": "48457"
  },
  {
    "issueNumber": "20240722010864",
    "number": "5",
    "colour": "green,violet",
    "premium": "93105"
  },
  {
    "issueNumber": "20240722010863",
    "number": "7",
    "colour": "green",
    "premium": "18557"
  },
  {
    "issueNumber": "20240722010862",
    "number": "7",
    "colour": "green",
    "premium": "77737"
  },
  {
    "issueNumber": "20240722010861",
    "number": "1",
    "colour": "green",
    "premium": "73041"
  },
  {
    "issueNumber": "20240722010860",
    "number": "5",
    "colour": "green,violet",
    "premium": "91075"
  },
  {
    "issueNumber": "20240722010859",
    "number": "7",
    "colour": "green",
    "premium": "15727"
  },
  {
    "issueNumber": "20240722010858",
    "number": "5",
    "colour": "green,violet",
    "premium": "74045"
  },
  {
    "issueNumber": "20240722010857",
    "number": "7",
    "colour": "green",
    "premium": "97127"
  },
  {
    "issueNumber": "20240722010856",
    "number": "9",
    "colour": "green",
    "premium": "27719"
  },
  {
    "issueNumber": "20240722010855",
    "number": "4",
    "colour": "red",
    "premium": "57314"
  },
  {
    "issueNumber": "20240722010854",
    "number": "7",
    "colour": "green",
    "premium": "51467"
  },
  {
    "issueNumber": "20240722010853",
    "number": "2",
    "colour": "red",
    "premium": "80932"
  },
  {
    "issueNumber": "20240722010852",
    "number": "3",
    "colour": "green",
    "premium": "48153"
  },
  {
    "issueNumber": "20240722010851",
    "number": "6",
    "colour": "red",
    "premium": "47366"
  },
  {
    "issueNumber": "20240722010850",
    "number": "9",
    "colour": "green",
    "premium": "33369"
  },
  {
    "issueNumber": "20240722010849",
    "number": "8",
    "colour": "red",
    "premium": "43058"
  },
  {
    "issueNumber": "20240722010848",
    "number": "0",
    "colour": "red,violet",
    "premium": "95170"
  },
  {
    "issueNumber": "20240722010847",
    "number": "9",
    "colour": "green",
    "premium": "43359"
  },
  {
    "issueNumber": "20240722010846",
    "number": "3",
    "colour": "green",
    "premium": "73603"
  },
  {
    "issueNumber": "20240722010845",
    "number": "3",
    "colour": "green",
    "premium": "28713"
  },
  {
    "issueNumber": "20240722010844",
    "number": "9",
    "colour": "green",
    "premium": "82039"
  },
  {
    "issueNumber": "20240722010843",
    "number": "9",
    "colour": "green",
    "premium": "22409"
  },
  {
    "issueNumber": "20240722010842",
    "number": "8",
    "colour": "red",
    "premium": "90668"
  },
  {
    "issueNumber": "20240722010841",
    "number": "3",
    "colour": "green",
    "premium": "56183"
  },
  {
    "issueNumber": "20240722010840",
    "number": "6",
    "colour": "red",
    "premium": "16086"
  },
  {
    "issueNumber": "20240722010839",
    "number": "7",
    "colour": "green",
    "premium": "70057"
  },
  {
    "issueNumber": "20240722010838",
    "number": "9",
    "colour": "green",
    "premium": "20499"
  },
  {
    "issueNumber": "20240722010837",
    "number": "5",
    "colour": "green,violet",
    "premium": "94055"
  },
  {
    "issueNumber": "20240722010836",
    "number": "0",
    "colour": "red,violet",
    "premium": "97960"
  },
  {
    "issueNumber": "20240722010835",
    "number": "1",
    "colour": "green",
    "premium": "41131"
  },
  {
    "issueNumber": "20240722010834",
    "number": "2",
    "colour": "red",
    "premium": "83252"
  },
  {
    "issueNumber": "20240722010833",
    "number": "5",
    "colour": "green,violet",
    "premium": "33695"
  },
  {
    "issueNumber": "20240722010832",
    "number": "2",
    "colour": "red",
    "premium": "55142"
  },
  {
    "issueNumber": "20240722010831",
    "number": "2",
    "colour": "red",
    "premium": "42502"
  },
  {
    "issueNumber": "20240722010830",
    "number": "4",
    "colour": "red",
    "premium": "35524"
  },
  {
    "issueNumber": "20240722010829",
    "number": "7",
    "colour": "green",
    "premium": "79907"
  },
  {
    "issueNumber": "20240722010828",
    "number": "9",
    "colour": "green",
    "premium": "42099"
  },
  {
    "issueNumber": "20240722010827",
    "number": "8",
    "colour": "red",
    "premium": "60258"
  },
  {
    "issueNumber": "20240722010826",
    "number": "6",
    "colour": "red",
    "premium": "55616"
  },
  {
    "issueNumber": "20240722010825",
    "number": "7",
    "colour": "green",
    "premium": "68397"
  },
  {
    "issueNumber": "20240722010824",
    "number": "9",
    "colour": "green",
    "premium": "32519"
  },
  {
    "issueNumber": "20240722010823",
    "number": "3",
    "colour": "green",
    "premium": "58563"
  },
  {
    "issueNumber": "20240722010822",
    "number": "4",
    "colour": "red",
    "premium": "61364"
  },
  {
    "issueNumber": "20240722010821",
    "number": "9",
    "colour": "green",
    "premium": "93309"
  },
  {
    "issueNumber": "20240722010820",
    "number": "9",
    "colour": "green",
    "premium": "79739"
  },
  {
    "issueNumber": "20240722010819",
    "number": "9",
    "colour": "green",
    "premium": "14289"
  },
  {
    "issueNumber": "20240722010818",
    "number": "6",
    "colour": "red",
    "premium": "81416"
  },
  {
    "issueNumber": "20240722010817",
    "number": "3",
    "colour": "green",
    "premium": "95523"
  },
  {
    "issueNumber": "20240722010816",
    "number": "4",
    "colour": "red",
    "premium": "93744"
  },
  {
    "issueNumber": "20240722010815",
    "number": "0",
    "colour": "red,violet",
    "premium": "39980"
  },
  {
    "issueNumber": "20240722010814",
    "number": "1",
    "colour": "green",
    "premium": "86521"
  },
  {
    "issueNumber": "20240722010813",
    "number": "1",
    "colour": "green",
    "premium": "33671"
  },
  {
    "issueNumber": "20240722010812",
    "number": "4",
    "colour": "red",
    "premium": "92054"
  },
  {
    "issueNumber": "20240722010811",
    "number": "7",
    "colour": "green",
    "premium": "60487"
  },
  {
    "issueNumber": "20240722010810",
    "number": "4",
    "colour": "red",
    "premium": "58734"
  },
  {
    "issueNumber": "20240722010809",
    "number": "8",
    "colour": "red",
    "premium": "40288"
  },
  {
    "issueNumber": "20240722010808",
    "number": "9",
    "colour": "green",
    "premium": "74179"
  },
  {
    "issueNumber": "20240722010807",
    "number": "7",
    "colour": "green",
    "premium": "23717"
  },
  {
    "issueNumber": "20240722010806",
    "number": "7",
    "colour": "green",
    "premium": "46047"
  },
  {
    "issueNumber": "20240722010805",
    "number": "4",
    "colour": "red",
    "premium": "66424"
  },
  {
    "issueNumber": "20240722010804",
    "number": "1",
    "colour": "green",
    "premium": "23201"
  },
  {
    "issueNumber": "20240722010803",
    "number": "5",
    "colour": "green,violet",
    "premium": "91575"
  },
  {
    "issueNumber": "20240722010802",
    "number": "1",
    "colour": "green",
    "premium": "86861"
  },
  {
    "issueNumber": "20240722010801",
    "number": "1",
    "colour": "green",
    "premium": "78061"
  },
  {
    "issueNumber": "20240722010800",
    "number": "6",
    "colour": "red",
    "premium": "34136"
  },
  {
    "issueNumber": "20240722010799",
    "number": "2",
    "colour": "red",
    "premium": "25602"
  },
  {
    "issueNumber": "20240722010798",
    "number": "9",
    "colour": "green",
    "premium": "28799"
  },
  {
    "issueNumber": "20240722010797",
    "number": "8",
    "colour": "red",
    "premium": "54008"
  },
  {
    "issueNumber": "20240722010796",
    "number": "0",
    "colour": "red,violet",
    "premium": "33530"
  },
  {
    "issueNumber": "20240722010795",
    "number": "5",
    "colour": "green,violet",
    "premium": "10995"
  },
  {
    "issueNumber": "20240722010794",
    "number": "5",
    "colour": "green,violet",
    "premium": "23145"
  },
  {
    "issueNumber": "20240722010793",
    "number": "2",
    "colour": "red",
    "premium": "92692"
  },
  {
    "issueNumber": "20240722010792",
    "number": "9",
    "colour": "green",
    "premium": "92149"
  },
  {
    "issueNumber": "20240722010791",
    "number": "5",
    "colour": "green,violet",
    "premium": "21695"
  },
  {
    "issueNumber": "20240722010790",
    "number": "0",
    "colour": "red,violet",
    "premium": "16700"
  },
  {
    "issueNumber": "20240722010789",
    "number": "6",
    "colour": "red",
    "premium": "48106"
  },
  {
    "issueNumber": "20240722010788",
    "number": "8",
    "colour": "red",
    "premium": "63108"
  },
  {
    "issueNumber": "20240722010787",
    "number": "8",
    "colour": "red",
    "premium": "34348"
  },
  {
    "issueNumber": "20240722010786",
    "number": "3",
    "colour": "green",
    "premium": "65993"
  },
  {
    "issueNumber": "20240722010785",
    "number": "2",
    "colour": "red",
    "premium": "14772"
  },
  {
    "issueNumber": "20240722010784",
    "number": "7",
    "colour": "green",
    "premium": "68027"
  },
  {
    "issueNumber": "20240722010783",
    "number": "7",
    "colour": "green",
    "premium": "62817"
  },
  {
    "issueNumber": "20240722010782",
    "number": "4",
    "colour": "red",
    "premium": "12054"
  },
  {
    "issueNumber": "20240722010781",
    "number": "9",
    "colour": "green",
    "premium": "48869"
  },
  {
    "issueNumber": "20240722010780",
    "number": "5",
    "colour": "green,violet",
    "premium": "41155"
  },
  {
    "issueNumber": "20240722010779",
    "number": "7",
    "colour": "green",
    "premium": "29027"
  },
  {
    "issueNumber": "20240722010778",
    "number": "1",
    "colour": "green",
    "premium": "53751"
  },
  {
    "issueNumber": "20240722010777",
    "number": "5",
    "colour": "green,violet",
    "premium": "20905"
  },
  {
    "issueNumber": "20240722010776",
    "number": "2",
    "colour": "red",
    "premium": "88772"
  },
  {
    "issueNumber": "20240722010775",
    "number": "2",
    "colour": "red",
    "premium": "12782"
  },
  {
    "issueNumber": "20240722010774",
    "number": "2",
    "colour": "red",
    "premium": "17172"
  },
  {
    "issueNumber": "20240722010773",
    "number": "9",
    "colour": "green",
    "premium": "33619"
  },
  {
    "issueNumber": "20240722010772",
    "number": "5",
    "colour": "green,violet",
    "premium": "25295"
  },
  {
    "issueNumber": "20240722010771",
    "number": "7",
    "colour": "green",
    "premium": "39867"
  },
  {
    "issueNumber": "20240722010770",
    "number": "3",
    "colour": "green",
    "premium": "65753"
  },
  {
    "issueNumber": "20240722010769",
    "number": "2",
    "colour": "red",
    "premium": "37762"
  },
  {
    "issueNumber": "20240722010768",
    "number": "0",
    "colour": "red,violet",
    "premium": "29630"
  },
  {
    "issueNumber": "20240722010767",
    "number": "3",
    "colour": "green",
    "premium": "70793"
  },
  {
    "issueNumber": "20240722010766",
    "number": "9",
    "colour": "green",
    "premium": "33979"
  },
  {
    "issueNumber": "20240722010765",
    "number": "2",
    "colour": "red",
    "premium": "22802"
  },
  {
    "issueNumber": "20240722010764",
    "number": "1",
    "colour": "green",
    "premium": "58441"
  },
  {
    "issueNumber": "20240722010763",
    "number": "8",
    "colour": "red",
    "premium": "97618"
  },
  {
    "issueNumber": "20240722010762",
    "number": "6",
    "colour": "red",
    "premium": "82966"
  },
  {
    "issueNumber": "20240722010761",
    "number": "3",
    "colour": "green",
    "premium": "78303"
  },
  {
    "issueNumber": "20240722010760",
    "number": "6",
    "colour": "red",
    "premium": "71016"
  },
  {
    "issueNumber": "20240722010759",
    "number": "0",
    "colour": "red,violet",
    "premium": "67140"
  },
  {
    "issueNumber": "20240722010758",
    "number": "1",
    "colour": "green",
    "premium": "12881"
  },
  {
    "issueNumber": "20240722010757",
    "number": "5",
    "colour": "green,violet",
    "premium": "52965"
  },
  {
    "issueNumber": "20240722010756",
    "number": "5",
    "colour": "green,violet",
    "premium": "13195"
  },
  {
    "issueNumber": "20240722010755",
    "number": "0",
    "colour": "red,violet",
    "premium": "10340"
  },
  {
    "issueNumber": "20240722010754",
    "number": "8",
    "colour": "red",
    "premium": "61368"
  },
  {
    "issueNumber": "20240722010753",
    "number": "0",
    "colour": "red,violet",
    "premium": "69530"
  },
  {
    "issueNumber": "20240722010752",
    "number": "6",
    "colour": "red",
    "premium": "68696"
  },
  {
    "issueNumber": "20240722010751",
    "number": "9",
    "colour": "green",
    "premium": "36229"
  },
  {
    "issueNumber": "20240722010750",
    "number": "7",
    "colour": "green",
    "premium": "78637"
  },
  {
    "issueNumber": "20240722010749",
    "number": "6",
    "colour": "red",
    "premium": "36266"
  },
  {
    "issueNumber": "20240722010748",
    "number": "3",
    "colour": "green",
    "premium": "38593"
  },
  {
    "issueNumber": "20240722010747",
    "number": "5",
    "colour": "green,violet",
    "premium": "99855"
  },
  {
    "issueNumber": "20240722010746",
    "number": "8",
    "colour": "red",
    "premium": "33578"
  },
  {
    "issueNumber": "20240722010745",
    "number": "0",
    "colour": "red,violet",
    "premium": "32020"
  },
  {
    "issueNumber": "20240722010744",
    "number": "8",
    "colour": "red",
    "premium": "63318"
  },
  {
    "issueNumber": "20240722010743",
    "number": "8",
    "colour": "red",
    "premium": "11508"
  },
  {
    "issueNumber": "20240722010742",
    "number": "0",
    "colour": "red,violet",
    "premium": "77330"
  },
  {
    "issueNumber": "20240722010741",
    "number": "8",
    "colour": "red",
    "premium": "38028"
  },
  {
    "issueNumber": "20240722010740",
    "number": "8",
    "colour": "red",
    "premium": "87648"
  },
  {
    "issueNumber": "20240722010739",
    "number": "4",
    "colour": "red",
    "premium": "35214"
  },
  {
    "issueNumber": "20240722010738",
    "number": "8",
    "colour": "red",
    "premium": "46468"
  },
  {
    "issueNumber": "20240722010737",
    "number": "8",
    "colour": "red",
    "premium": "55138"
  },
  {
    "issueNumber": "20240722010736",
    "number": "6",
    "colour": "red",
    "premium": "97986"
  },
  {
    "issueNumber": "20240722010735",
    "number": "3",
    "colour": "green",
    "premium": "39213"
  },
  {
    "issueNumber": "20240722010734",
    "number": "7",
    "colour": "green",
    "premium": "20627"
  },
  {
    "issueNumber": "20240722010733",
    "number": "2",
    "colour": "red",
    "premium": "67332"
  },
  {
    "issueNumber": "20240722010732",
    "number": "5",
    "colour": "green,violet",
    "premium": "81225"
  },
  {
    "issueNumber": "20240722010731",
    "number": "3",
    "colour": "green",
    "premium": "15463"
  },
  {
    "issueNumber": "20240722010730",
    "number": "9",
    "colour": "green",
    "premium": "62239"
  },
  {
    "issueNumber": "20240722010729",
    "number": "0",
    "colour": "red,violet",
    "premium": "75990"
  },
  {
    "issueNumber": "20240722010728",
    "number": "2",
    "colour": "red",
    "premium": "11602"
  },
  {
    "issueNumber": "20240722010727",
    "number": "4",
    "colour": "red",
    "premium": "24504"
  },
  {
    "issueNumber": "20240722010726",
    "number": "9",
    "colour": "green",
    "premium": "97449"
  },
  {
    "issueNumber": "20240722010725",
    "number": "2",
    "colour": "red",
    "premium": "74392"
  },
  {
    "issueNumber": "20240722010724",
    "number": "4",
    "colour": "red",
    "premium": "14424"
  },
  {
    "issueNumber": "20240722010723",
    "number": "1",
    "colour": "green",
    "premium": "27931"
  },
  {
    "issueNumber": "20240722010722",
    "number": "6",
    "colour": "red",
    "premium": "59996"
  },
  {
    "issueNumber": "20240722010721",
    "number": "4",
    "colour": "red",
    "premium": "78544"
  },
  {
    "issueNumber": "20240722010720",
    "number": "1",
    "colour": "green",
    "premium": "90781"
  },
  {
    "issueNumber": "20240722010719",
    "number": "8",
    "colour": "red",
    "premium": "95658"
  },
  {
    "issueNumber": "20240722010718",
    "number": "8",
    "colour": "red",
    "premium": "36488"
  },
  {
    "issueNumber": "20240722010717",
    "number": "5",
    "colour": "green,violet",
    "premium": "57575"
  },
  {
    "issueNumber": "20240722010716",
    "number": "6",
    "colour": "red",
    "premium": "88166"
  },
  {
    "issueNumber": "20240722010715",
    "number": "7",
    "colour": "green",
    "premium": "13807"
  },
  {
    "issueNumber": "20240722010714",
    "number": "1",
    "colour": "green",
    "premium": "23421"
  },
  {
    "issueNumber": "20240722010713",
    "number": "3",
    "colour": "green",
    "premium": "23793"
  },
  {
    "issueNumber": "20240722010712",
    "number": "1",
    "colour": "green",
    "premium": "95561"
  },
  {
    "issueNumber": "20240722010711",
    "number": "8",
    "colour": "red",
    "premium": "82588"
  },
  {
    "issueNumber": "20240722010710",
    "number": "4",
    "colour": "red",
    "premium": "46284"
  },
  {
    "issueNumber": "20240722010709",
    "number": "6",
    "colour": "red",
    "premium": "90356"
  },
  {
    "issueNumber": "20240722010708",
    "number": "7",
    "colour": "green",
    "premium": "40067"
  },
  {
    "issueNumber": "20240722010707",
    "number": "2",
    "colour": "red",
    "premium": "27102"
  },
  {
    "issueNumber": "20240722010706",
    "number": "4",
    "colour": "red",
    "premium": "26804"
  },
  {
    "issueNumber": "20240722010705",
    "number": "6",
    "colour": "red",
    "premium": "23366"
  },
  {
    "issueNumber": "20240722010704",
    "number": "4",
    "colour": "red",
    "premium": "87544"
  },
  {
    "issueNumber": "20240722010703",
    "number": "0",
    "colour": "red,violet",
    "premium": "99190"
  },
  {
    "issueNumber": "20240722010702",
    "number": "9",
    "colour": "green",
    "premium": "84879"
  },
  {
    "issueNumber": "20240722010701",
    "number": "5",
    "colour": "green,violet",
    "premium": "28975"
  },
  {
    "issueNumber": "20240722010700",
    "number": "3",
    "colour": "green",
    "premium": "15733"
  },
  {
    "issueNumber": "20240722010699",
    "number": "1",
    "colour": "green",
    "premium": "54881"
  },
  {
    "issueNumber": "20240722010698",
    "number": "8",
    "colour": "red",
    "premium": "82838"
  },
  {
    "issueNumber": "20240722010697",
    "number": "4",
    "colour": "red",
    "premium": "91694"
  },
  {
    "issueNumber": "20240722010696",
    "number": "4",
    "colour": "red",
    "premium": "98904"
  },
  {
    "issueNumber": "20240722010695",
    "number": "7",
    "colour": "green",
    "premium": "57987"
  },
  {
    "issueNumber": "20240722010694",
    "number": "0",
    "colour": "red,violet",
    "premium": "17070"
  },
  {
    "issueNumber": "20240722010693",
    "number": "1",
    "colour": "green",
    "premium": "80091"
  },
  {
    "issueNumber": "20240722010692",
    "number": "4",
    "colour": "red",
    "premium": "43264"
  },
  {
    "issueNumber": "20240722010691",
    "number": "1",
    "colour": "green",
    "premium": "76711"
  },
  {
    "issueNumber": "20240722010690",
    "number": "5",
    "colour": "green,violet",
    "premium": "89485"
  },
  {
    "issueNumber": "20240722010689",
    "number": "5",
    "colour": "green,violet",
    "premium": "12555"
  },
  {
    "issueNumber": "20240722010688",
    "number": "6",
    "colour": "red",
    "premium": "49806"
  },
  {
    "issueNumber": "20240722010687",
    "number": "1",
    "colour": "green",
    "premium": "99811"
  },
  {
    "issueNumber": "20240722010686",
    "number": "9",
    "colour": "green",
    "premium": "59369"
  },
  {
    "issueNumber": "20240722010685",
    "number": "5",
    "colour": "green,violet",
    "premium": "24725"
  },
  {
    "issueNumber": "20240722010684",
    "number": "7",
    "colour": "green",
    "premium": "13697"
  },
  {
    "issueNumber": "20240722010683",
    "number": "1",
    "colour": "green",
    "premium": "90981"
  },
  {
    "issueNumber": "20240722010682",
    "number": "5",
    "colour": "green,violet",
    "premium": "66045"
  },
  {
    "issueNumber": "20240722010681",
    "number": "1",
    "colour": "green",
    "premium": "38611"
  },
  {
    "issueNumber": "20240722010680",
    "number": "8",
    "colour": "red",
    "premium": "78608"
  },
  {
    "issueNumber": "20240722010679",
    "number": "3",
    "colour": "green",
    "premium": "19543"
  },
  {
    "issueNumber": "20240722010678",
    "number": "6",
    "colour": "red",
    "premium": "91656"
  },
  {
    "issueNumber": "20240722010677",
    "number": "6",
    "colour": "red",
    "premium": "64006"
  },
  {
    "issueNumber": "20240722010676",
    "number": "0",
    "colour": "red,violet",
    "premium": "91740"
  },
  {
    "issueNumber": "20240722010675",
    "number": "2",
    "colour": "red",
    "premium": "99172"
  },
  {
    "issueNumber": "20240722010674",
    "number": "4",
    "colour": "red",
    "premium": "22944"
  },
  {
    "issueNumber": "20240722010673",
    "number": "3",
    "colour": "green",
    "premium": "38093"
  },
  {
    "issueNumber": "20240722010672",
    "number": "0",
    "colour": "red,violet",
    "premium": "28050"
  },
  {
    "issueNumber": "20240722010671",
    "number": "5",
    "colour": "green,violet",
    "premium": "90845"
  },
  {
    "issueNumber": "20240722010670",
    "number": "2",
    "colour": "red",
    "premium": "15412"
  },
  {
    "issueNumber": "20240722010669",
    "number": "1",
    "colour": "green",
    "premium": "14681"
  },
  {
    "issueNumber": "20240722010668",
    "number": "0",
    "colour": "red,violet",
    "premium": "16250"
  },
  {
    "issueNumber": "20240722010667",
    "number": "7",
    "colour": "green",
    "premium": "27527"
  },
  {
    "issueNumber": "20240722010666",
    "number": "3",
    "colour": "green",
    "premium": "48783"
  },
  {
    "issueNumber": "20240722010665",
    "number": "3",
    "colour": "green",
    "premium": "65533"
  },
  {
    "issueNumber": "20240722010664",
    "number": "2",
    "colour": "red",
    "premium": "68152"
  },
  {
    "issueNumber": "20240722010663",
    "number": "6",
    "colour": "red",
    "premium": "19556"
  },
  {
    "issueNumber": "20240722010662",
    "number": "1",
    "colour": "green",
    "premium": "59661"
  },
  {
    "issueNumber": "20240722010661",
    "number": "7",
    "colour": "green",
    "premium": "85107"
  },
  {
    "issueNumber": "20240722010660",
    "number": "1",
    "colour": "green",
    "premium": "58391"
  },
  {
    "issueNumber": "20240722010659",
    "number": "9",
    "colour": "green",
    "premium": "37129"
  },
  {
    "issueNumber": "20240722010658",
    "number": "4",
    "colour": "red",
    "premium": "73864"
  },
  {
    "issueNumber": "20240722010657",
    "number": "6",
    "colour": "red",
    "premium": "43956"
  },
  {
    "issueNumber": "20240722010656",
    "number": "0",
    "colour": "red,violet",
    "premium": "60500"
  },
  {
    "issueNumber": "20240722010655",
    "number": "0",
    "colour": "red,violet",
    "premium": "65010"
  },
  {
    "issueNumber": "20240722010654",
    "number": "4",
    "colour": "red",
    "premium": "24014"
  },
  {
    "issueNumber": "20240722010653",
    "number": "5",
    "colour": "green,violet",
    "premium": "14475"
  },
  {
    "issueNumber": "20240722010652",
    "number": "4",
    "colour": "red",
    "premium": "95774"
  },
  {
    "issueNumber": "20240722010651",
    "number": "8",
    "colour": "red",
    "premium": "23968"
  },
  {
    "issueNumber": "20240722010650",
    "number": "2",
    "colour": "red",
    "premium": "68312"
  },
  {
    "issueNumber": "20240722010649",
    "number": "9",
    "colour": "green",
    "premium": "16649"
  },
  {
    "issueNumber": "20240722010648",
    "number": "8",
    "colour": "red",
    "premium": "82968"
  },
  {
    "issueNumber": "20240722010647",
    "number": "5",
    "colour": "green,violet",
    "premium": "97205"
  },
  {
    "issueNumber": "20240722010646",
    "number": "1",
    "colour": "green",
    "premium": "89931"
  },
  {
    "issueNumber": "20240722010645",
    "number": "8",
    "colour": "red",
    "premium": "63978"
  },
  {
    "issueNumber": "20240722010644",
    "number": "8",
    "colour": "red",
    "premium": "16948"
  },
  {
    "issueNumber": "20240722010643",
    "number": "3",
    "colour": "green",
    "premium": "62463"
  },
  {
    "issueNumber": "20240722010642",
    "number": "5",
    "colour": "green,violet",
    "premium": "77485"
  },
  {
    "issueNumber": "20240722010641",
    "number": "0",
    "colour": "red,violet",
    "premium": "15680"
  },
  {
    "issueNumber": "20240722010640",
    "number": "0",
    "colour": "red,violet",
    "premium": "56070"
  },
  {
    "issueNumber": "20240722010639",
    "number": "6",
    "colour": "red",
    "premium": "95846"
  },
  {
    "issueNumber": "20240722010638",
    "number": "0",
    "colour": "red,violet",
    "premium": "98440"
  },
  {
    "issueNumber": "20240722010637",
    "number": "9",
    "colour": "green",
    "premium": "69889"
  },
  {
    "issueNumber": "20240722010636",
    "number": "0",
    "colour": "red,violet",
    "premium": "96680"
  },
  {
    "issueNumber": "20240722010635",
    "number": "4",
    "colour": "red",
    "premium": "77834"
  },
  {
    "issueNumber": "20240722010634",
    "number": "9",
    "colour": "green",
    "premium": "70359"
  },
  {
    "issueNumber": "20240722010633",
    "number": "5",
    "colour": "green,violet",
    "premium": "61825"
  },
  {
    "issueNumber": "20240722010632",
    "number": "1",
    "colour": "green",
    "premium": "52041"
  },
  {
    "issueNumber": "20240722010631",
    "number": "5",
    "colour": "green,violet",
    "premium": "12815"
  },
  {
    "issueNumber": "20240722010630",
    "number": "3",
    "colour": "green",
    "premium": "51103"
  },
  {
    "issueNumber": "20240722010629",
    "number": "0",
    "colour": "red,violet",
    "premium": "90960"
  },
  {
    "issueNumber": "20240722010628",
    "number": "2",
    "colour": "red",
    "premium": "71382"
  },
  {
    "issueNumber": "20240722010627",
    "number": "3",
    "colour": "green",
    "premium": "59003"
  },
  {
    "issueNumber": "20240722010626",
    "number": "7",
    "colour": "green",
    "premium": "65507"
  },
  {
    "issueNumber": "20240722010625",
    "number": "1",
    "colour": "green",
    "premium": "93151"
  },
  {
    "issueNumber": "20240722010624",
    "number": "9",
    "colour": "green",
    "premium": "82309"
  },
  {
    "issueNumber": "20240722010623",
    "number": "4",
    "colour": "red",
    "premium": "10864"
  },
  {
    "issueNumber": "20240722010622",
    "number": "1",
    "colour": "green",
    "premium": "53001"
  },
  {
    "issueNumber": "20240722010621",
    "number": "5",
    "colour": "green,violet",
    "premium": "59455"
  },
  {
    "issueNumber": "20240722010620",
    "number": "9",
    "colour": "green",
    "premium": "64189"
  },
  {
    "issueNumber": "20240722010619",
    "number": "8",
    "colour": "red",
    "premium": "52588"
  },
  {
    "issueNumber": "20240722010618",
    "number": "3",
    "colour": "green",
    "premium": "58443"
  },
  {
    "issueNumber": "20240722010617",
    "number": "6",
    "colour": "red",
    "premium": "57736"
  },
  {
    "issueNumber": "20240722010616",
    "number": "0",
    "colour": "red,violet",
    "premium": "95780"
  },
  {
    "issueNumber": "20240722010615",
    "number": "5",
    "colour": "green,violet",
    "premium": "51585"
  },
  {
    "issueNumber": "20240722010614",
    "number": "0",
    "colour": "red,violet",
    "premium": "96210"
  },
  {
    "issueNumber": "20240722010613",
    "number": "3",
    "colour": "green",
    "premium": "99653"
  },
  {
    "issueNumber": "20240722010612",
    "number": "5",
    "colour": "green,violet",
    "premium": "92445"
  },
  {
    "issueNumber": "20240722010611",
    "number": "7",
    "colour": "green",
    "premium": "50647"
  },
  {
    "issueNumber": "20240722010610",
    "number": "7",
    "colour": "green",
    "premium": "50367"
  },
  {
    "issueNumber": "20240722010609",
    "number": "8",
    "colour": "red",
    "premium": "15468"
  },
  {
    "issueNumber": "20240722010608",
    "number": "7",
    "colour": "green",
    "premium": "35857"
  },
  {
    "issueNumber": "20240722010607",
    "number": "2",
    "colour": "red",
    "premium": "85192"
  },
  {
    "issueNumber": "20240722010606",
    "number": "4",
    "colour": "red",
    "premium": "62704"
  },
  {
    "issueNumber": "20240722010605",
    "number": "3",
    "colour": "green",
    "premium": "51963"
  },
  {
    "issueNumber": "20240722010604",
    "number": "0",
    "colour": "red,violet",
    "premium": "29410"
  },
  {
    "issueNumber": "20240722010603",
    "number": "8",
    "colour": "red",
    "premium": "72438"
  },
  {
    "issueNumber": "20240722010602",
    "number": "1",
    "colour": "green",
    "premium": "54181"
  },
  {
    "issueNumber": "20240722010601",
    "number": "3",
    "colour": "green",
    "premium": "41403"
  },
  {
    "issueNumber": "20240722010600",
    "number": "6",
    "colour": "red",
    "premium": "75236"
  },
  {
    "issueNumber": "20240722010599",
    "number": "7",
    "colour": "green",
    "premium": "92067"
  },
  {
    "issueNumber": "20240722010598",
    "number": "4",
    "colour": "red",
    "premium": "63874"
  },
  {
    "issueNumber": "20240722010597",
    "number": "8",
    "colour": "red",
    "premium": "48428"
  },
  {
    "issueNumber": "20240722010596",
    "number": "3",
    "colour": "green",
    "premium": "77263"
  },
  {
    "issueNumber": "20240722010595",
    "number": "4",
    "colour": "red",
    "premium": "26164"
  },
  {
    "issueNumber": "20240722010594",
    "number": "7",
    "colour": "green",
    "premium": "27367"
  },
  {
    "issueNumber": "20240722010593",
    "number": "8",
    "colour": "red",
    "premium": "46318"
  },
  {
    "issueNumber": "20240722010592",
    "number": "5",
    "colour": "green,violet",
    "premium": "71265"
  },
  {
    "issueNumber": "20240722010591",
    "number": "8",
    "colour": "red",
    "premium": "24468"
  },
  {
    "issueNumber": "20240722010590",
    "number": "0",
    "colour": "red,violet",
    "premium": "99410"
  },
  {
    "issueNumber": "20240722010589",
    "number": "5",
    "colour": "green,violet",
    "premium": "96425"
  },
  {
    "issueNumber": "20240722010588",
    "number": "4",
    "colour": "red",
    "premium": "95574"
  },
  {
    "issueNumber": "20240722010587",
    "number": "3",
    "colour": "green",
    "premium": "83233"
  },
  {
    "issueNumber": "20240722010586",
    "number": "8",
    "colour": "red",
    "premium": "80978"
  },
  {
    "issueNumber": "20240722010585",
    "number": "7",
    "colour": "green",
    "premium": "30447"
  },
  {
    "issueNumber": "20240722010584",
    "number": "9",
    "colour": "green",
    "premium": "89969"
  },
  {
    "issueNumber": "20240722010583",
    "number": "0",
    "colour": "red,violet",
    "premium": "34870"
  },
  {
    "issueNumber": "20240722010582",
    "number": "3",
    "colour": "green",
    "premium": "18253"
  },
  {
    "issueNumber": "20240722010581",
    "number": "6",
    "colour": "red",
    "premium": "30526"
  },
  {
    "issueNumber": "20240722010580",
    "number": "0",
    "colour": "red,violet",
    "premium": "45670"
  },
  {
    "issueNumber": "20240722010579",
    "number": "4",
    "colour": "red",
    "premium": "32954"
  },
  {
    "issueNumber": "20240722010578",
    "number": "5",
    "colour": "green,violet",
    "premium": "95565"
  },
  {
    "issueNumber": "20240722010577",
    "number": "6",
    "colour": "red",
    "premium": "63456"
  },
  {
    "issueNumber": "20240722010576",
    "number": "2",
    "colour": "red",
    "premium": "49122"
  },
  {
    "issueNumber": "20240722010575",
    "number": "5",
    "colour": "green,violet",
    "premium": "42675"
  },
  {
    "issueNumber": "20240722010574",
    "number": "3",
    "colour": "green",
    "premium": "93133"
  },
  {
    "issueNumber": "20240722010573",
    "number": "1",
    "colour": "green",
    "premium": "86881"
  },
  {
    "issueNumber": "20240722010572",
    "number": "1",
    "colour": "green",
    "premium": "87361"
  },
  {
    "issueNumber": "20240722010571",
    "number": "3",
    "colour": "green",
    "premium": "19943"
  },
  {
    "issueNumber": "20240722010570",
    "number": "7",
    "colour": "green",
    "premium": "64977"
  },
  {
    "issueNumber": "20240722010569",
    "number": "8",
    "colour": "red",
    "premium": "92098"
  },
  {
    "issueNumber": "20240722010568",
    "number": "2",
    "colour": "red",
    "premium": "53662"
  },
  {
    "issueNumber": "20240722010567",
    "number": "7",
    "colour": "green",
    "premium": "23187"
  },
  {
    "issueNumber": "20240722010566",
    "number": "1",
    "colour": "green",
    "premium": "97121"
  },
  {
    "issueNumber": "20240722010565",
    "number": "3",
    "colour": "green",
    "premium": "27383"
  },
  {
    "issueNumber": "20240722010564",
    "number": "1",
    "colour": "green",
    "premium": "91221"
  },
  {
    "issueNumber": "20240722010563",
    "number": "0",
    "colour": "red,violet",
    "premium": "37390"
  },
  {
    "issueNumber": "20240722010562",
    "number": "1",
    "colour": "green",
    "premium": "49941"
  },
  {
    "issueNumber": "20240722010561",
    "number": "7",
    "colour": "green",
    "premium": "46187"
  },
  {
    "issueNumber": "20240722010560",
    "number": "4",
    "colour": "red",
    "premium": "28564"
  },
  {
    "issueNumber": "20240722010559",
    "number": "1",
    "colour": "green",
    "premium": "49861"
  },
  {
    "issueNumber": "20240722010558",
    "number": "1",
    "colour": "green",
    "premium": "66491"
  },
  {
    "issueNumber": "20240722010557",
    "number": "6",
    "colour": "red",
    "premium": "39686"
  },
  {
    "issueNumber": "20240722010556",
    "number": "0",
    "colour": "red,violet",
    "premium": "91460"
  },
  {
    "issueNumber": "20240722010555",
    "number": "2",
    "colour": "red",
    "premium": "81932"
  },
  {
    "issueNumber": "20240722010554",
    "number": "7",
    "colour": "green",
    "premium": "86767"
  },
  {
    "issueNumber": "20240722010553",
    "number": "0",
    "colour": "red,violet",
    "premium": "26410"
  },
  {
    "issueNumber": "20240722010552",
    "number": "3",
    "colour": "green",
    "premium": "61413"
  },
  {
    "issueNumber": "20240722010551",
    "number": "2",
    "colour": "red",
    "premium": "60502"
  },
  {
    "issueNumber": "20240722010550",
    "number": "0",
    "colour": "red,violet",
    "premium": "46080"
  },
  {
    "issueNumber": "20240722010549",
    "number": "9",
    "colour": "green",
    "premium": "62069"
  },
  {
    "issueNumber": "20240722010548",
    "number": "4",
    "colour": "red",
    "premium": "46224"
  },
  {
    "issueNumber": "20240722010547",
    "number": "7",
    "colour": "green",
    "premium": "66297"
  },
  {
    "issueNumber": "20240722010546",
    "number": "9",
    "colour": "green",
    "premium": "42519"
  },
  {
    "issueNumber": "20240722010545",
    "number": "3",
    "colour": "green",
    "premium": "29573"
  },
  {
    "issueNumber": "20240722010544",
    "number": "4",
    "colour": "red",
    "premium": "72614"
  },
  {
    "issueNumber": "20240722010543",
    "number": "4",
    "colour": "red",
    "premium": "15184"
  },
  {
    "issueNumber": "20240722010542",
    "number": "1",
    "colour": "green",
    "premium": "86681"
  },
  {
    "issueNumber": "20240722010541",
    "number": "3",
    "colour": "green",
    "premium": "93473"
  },
  {
    "issueNumber": "20240722010540",
    "number": "2",
    "colour": "red",
    "premium": "65562"
  },
  {
    "issueNumber": "20240722010539",
    "number": "4",
    "colour": "red",
    "premium": "16194"
  },
  {
    "issueNumber": "20240722010538",
    "number": "4",
    "colour": "red",
    "premium": "69724"
  },
  {
    "issueNumber": "20240722010537",
    "number": "0",
    "colour": "red,violet",
    "premium": "26200"
  },
  {
    "issueNumber": "20240722010536",
    "number": "4",
    "colour": "red",
    "premium": "40634"
  },
  {
    "issueNumber": "20240722010535",
    "number": "0",
    "colour": "red,violet",
    "premium": "55040"
  },
  {
    "issueNumber": "20240722010534",
    "number": "4",
    "colour": "red",
    "premium": "38314"
  },
  {
    "issueNumber": "20240722010533",
    "number": "1",
    "colour": "green",
    "premium": "53321"
  },
  {
    "issueNumber": "20240722010532",
    "number": "0",
    "colour": "red,violet",
    "premium": "16370"
  },
  {
    "issueNumber": "20240722010531",
    "number": "2",
    "colour": "red",
    "premium": "10852"
  },
  {
    "issueNumber": "20240722010530",
    "number": "1",
    "colour": "green",
    "premium": "62401"
  },
  {
    "issueNumber": "20240722010529",
    "number": "4",
    "colour": "red",
    "premium": "24274"
  },
  {
    "issueNumber": "20240722010528",
    "number": "0",
    "colour": "red,violet",
    "premium": "13410"
  },
  {
    "issueNumber": "20240722010527",
    "number": "4",
    "colour": "red",
    "premium": "54584"
  },
  {
    "issueNumber": "20240722010526",
    "number": "6",
    "colour": "red",
    "premium": "25896"
  },
  {
    "issueNumber": "20240722010525",
    "number": "8",
    "colour": "red",
    "premium": "34598"
  },
  {
    "issueNumber": "20240722010524",
    "number": "9",
    "colour": "green",
    "premium": "10719"
  },
  {
    "issueNumber": "20240722010523",
    "number": "5",
    "colour": "green,violet",
    "premium": "93415"
  },
  {
    "issueNumber": "20240722010522",
    "number": "6",
    "colour": "red",
    "premium": "21876"
  },
  {
    "issueNumber": "20240722010521",
    "number": "2",
    "colour": "red",
    "premium": "77052"
  },
  {
    "issueNumber": "20240722010520",
    "number": "6",
    "colour": "red",
    "premium": "60876"
  },
  {
    "issueNumber": "20240722010519",
    "number": "2",
    "colour": "red",
    "premium": "75562"
  },
  {
    "issueNumber": "20240722010518",
    "number": "3",
    "colour": "green",
    "premium": "27443"
  },
  {
    "issueNumber": "20240722010517",
    "number": "0",
    "colour": "red,violet",
    "premium": "11600"
  },
  {
    "issueNumber": "20240722010516",
    "number": "3",
    "colour": "green",
    "premium": "80583"
  },
  {
    "issueNumber": "20240722010515",
    "number": "0",
    "colour": "red,violet",
    "premium": "35310"
  },
  {
    "issueNumber": "20240722010514",
    "number": "1",
    "colour": "green",
    "premium": "52851"
  },
  {
    "issueNumber": "20240722010513",
    "number": "4",
    "colour": "red",
    "premium": "60404"
  },
  {
    "issueNumber": "20240722010512",
    "number": "5",
    "colour": "green,violet",
    "premium": "43915"
  },
  {
    "issueNumber": "20240722010511",
    "number": "4",
    "colour": "red",
    "premium": "99604"
  },
  {
    "issueNumber": "20240722010510",
    "number": "8",
    "colour": "red",
    "premium": "56188"
  },
  {
    "issueNumber": "20240722010509",
    "number": "5",
    "colour": "green,violet",
    "premium": "79485"
  },
  {
    "issueNumber": "20240722010508",
    "number": "7",
    "colour": "green",
    "premium": "65387"
  },
  {
    "issueNumber": "20240722010507",
    "number": "9",
    "colour": "green",
    "premium": "47039"
  },
  {
    "issueNumber": "20240722010506",
    "number": "1",
    "colour": "green",
    "premium": "57491"
  },
  {
    "issueNumber": "20240722010505",
    "number": "9",
    "colour": "green",
    "premium": "26799"
  },
  {
    "issueNumber": "20240722010504",
    "number": "2",
    "colour": "red",
    "premium": "19082"
  },
  {
    "issueNumber": "20240722010503",
    "number": "2",
    "colour": "red",
    "premium": "11972"
  },
  {
    "issueNumber": "20240722010502",
    "number": "7",
    "colour": "green",
    "premium": "21757"
  },
  {
    "issueNumber": "20240722010501",
    "number": "9",
    "colour": "green",
    "premium": "93819"
  },
  {
    "issueNumber": "20240722010500",
    "number": "1",
    "colour": "green",
    "premium": "26621"
  },
  {
    "issueNumber": "20240722010499",
    "number": "8",
    "colour": "red",
    "premium": "68258"
  },
  {
    "issueNumber": "20240722010498",
    "number": "4",
    "colour": "red",
    "premium": "66104"
  },
  {
    "issueNumber": "20240722010497",
    "number": "3",
    "colour": "green",
    "premium": "87963"
  },
  {
    "issueNumber": "20240722010496",
    "number": "2",
    "colour": "red",
    "premium": "68772"
  },
  {
    "issueNumber": "20240722010495",
    "number": "8",
    "colour": "red",
    "premium": "57128"
  },
  {
    "issueNumber": "20240722010494",
    "number": "3",
    "colour": "green",
    "premium": "64773"
  },
  {
    "issueNumber": "20240722010493",
    "number": "3",
    "colour": "green",
    "premium": "19093"
  },
  {
    "issueNumber": "20240722010492",
    "number": "8",
    "colour": "red",
    "premium": "93628"
  },
  {
    "issueNumber": "20240722010491",
    "number": "1",
    "colour": "green",
    "premium": "42961"
  },
  {
    "issueNumber": "20240722010490",
    "number": "6",
    "colour": "red",
    "premium": "82076"
  },
  {
    "issueNumber": "20240722010489",
    "number": "4",
    "colour": "red",
    "premium": "93454"
  },
  {
    "issueNumber": "20240722010488",
    "number": "0",
    "colour": "red,violet",
    "premium": "56910"
  },
  {
    "issueNumber": "20240722010487",
    "number": "5",
    "colour": "green,violet",
    "premium": "39005"
  },
  {
    "issueNumber": "20240722010486",
    "number": "4",
    "colour": "red",
    "premium": "38864"
  },
  {
    "issueNumber": "20240722010485",
    "number": "9",
    "colour": "green",
    "premium": "71839"
  },
  {
    "issueNumber": "20240722010484",
    "number": "9",
    "colour": "green",
    "premium": "47329"
  },
  {
    "issueNumber": "20240722010483",
    "number": "1",
    "colour": "green",
    "premium": "87931"
  },
  {
    "issueNumber": "20240722010482",
    "number": "1",
    "colour": "green",
    "premium": "28261"
  },
  {
    "issueNumber": "20240722010481",
    "number": "3",
    "colour": "green",
    "premium": "74133"
  },
  {
    "issueNumber": "20240722010480",
    "number": "2",
    "colour": "red",
    "premium": "44262"
  },
  {
    "issueNumber": "20240722010479",
    "number": "9",
    "colour": "green",
    "premium": "77229"
  },
  {
    "issueNumber": "20240722010478",
    "number": "5",
    "colour": "green,violet",
    "premium": "22735"
  },
  {
    "issueNumber": "20240722010477",
    "number": "0",
    "colour": "red,violet",
    "premium": "94120"
  },
  {
    "issueNumber": "20240722010476",
    "number": "4",
    "colour": "red",
    "premium": "86464"
  },
  {
    "issueNumber": "20240722010475",
    "number": "4",
    "colour": "red",
    "premium": "56294"
  },
  {
    "issueNumber": "20240722010474",
    "number": "5",
    "colour": "green,violet",
    "premium": "92725"
  },
  {
    "issueNumber": "20240722010473",
    "number": "1",
    "colour": "green",
    "premium": "44001"
  },
  {
    "issueNumber": "20240722010472",
    "number": "1",
    "colour": "green",
    "premium": "12281"
  },
  {
    "issueNumber": "20240722010471",
    "number": "9",
    "colour": "green",
    "premium": "65099"
  },
  {
    "issueNumber": "20240722010470",
    "number": "1",
    "colour": "green",
    "premium": "89981"
  },
  {
    "issueNumber": "20240722010469",
    "number": "5",
    "colour": "green,violet",
    "premium": "98715"
  },
  {
    "issueNumber": "20240722010468",
    "number": "8",
    "colour": "red",
    "premium": "87528"
  },
  {
    "issueNumber": "20240722010467",
    "number": "6",
    "colour": "red",
    "premium": "47016"
  },
  {
    "issueNumber": "20240722010466",
    "number": "0",
    "colour": "red,violet",
    "premium": "64660"
  },
  {
    "issueNumber": "20240722010465",
    "number": "7",
    "colour": "green",
    "premium": "95677"
  },
  {
    "issueNumber": "20240722010464",
    "number": "1",
    "colour": "green",
    "premium": "52731"
  },
  {
    "issueNumber": "20240722010463",
    "number": "0",
    "colour": "red,violet",
    "premium": "37570"
  },
  {
    "issueNumber": "20240722010462",
    "number": "9",
    "colour": "green",
    "premium": "48239"
  },
  {
    "issueNumber": "20240722010461",
    "number": "5",
    "colour": "green,violet",
    "premium": "28355"
  },
  {
    "issueNumber": "20240722010460",
    "number": "0",
    "colour": "red,violet",
    "premium": "83070"
  },
  {
    "issueNumber": "20240722010459",
    "number": "3",
    "colour": "green",
    "premium": "66103"
  },
  {
    "issueNumber": "20240722010458",
    "number": "0",
    "colour": "red,violet",
    "premium": "37700"
  },
  {
    "issueNumber": "20240722010457",
    "number": "2",
    "colour": "red",
    "premium": "12902"
  },
  {
    "issueNumber": "20240722010456",
    "number": "7",
    "colour": "green",
    "premium": "47857"
  },
  {
    "issueNumber": "20240722010455",
    "number": "6",
    "colour": "red",
    "premium": "86986"
  },
  {
    "issueNumber": "20240722010454",
    "number": "9",
    "colour": "green",
    "premium": "62239"
  },
  {
    "issueNumber": "20240722010453",
    "number": "7",
    "colour": "green",
    "premium": "30027"
  },
  {
    "issueNumber": "20240722010452",
    "number": "3",
    "colour": "green",
    "premium": "23623"
  },
  {
    "issueNumber": "20240722010451",
    "number": "4",
    "colour": "red",
    "premium": "43754"
  },
  {
    "issueNumber": "20240722010450",
    "number": "9",
    "colour": "green",
    "premium": "66869"
  },
  {
    "issueNumber": "20240722010449",
    "number": "2",
    "colour": "red",
    "premium": "84242"
  },
  {
    "issueNumber": "20240722010448",
    "number": "5",
    "colour": "green,violet",
    "premium": "82925"
  },
  {
    "issueNumber": "20240722010447",
    "number": "2",
    "colour": "red",
    "premium": "77102"
  },
  {
    "issueNumber": "20240722010446",
    "number": "5",
    "colour": "green,violet",
    "premium": "60265"
  },
  {
    "issueNumber": "20240722010445",
    "number": "2",
    "colour": "red",
    "premium": "63692"
  },
  {
    "issueNumber": "20240722010444",
    "number": "1",
    "colour": "green",
    "premium": "55511"
  },
  {
    "issueNumber": "20240722010443",
    "number": "3",
    "colour": "green",
    "premium": "56583"
  },
  {
    "issueNumber": "20240722010442",
    "number": "0",
    "colour": "red,violet",
    "premium": "67010"
  },
  {
    "issueNumber": "20240722010441",
    "number": "6",
    "colour": "red",
    "premium": "27266"
  },
  {
    "issueNumber": "20240722010440",
    "number": "3",
    "colour": "green",
    "premium": "73673"
  },
  {
    "issueNumber": "20240722010439",
    "number": "9",
    "colour": "green",
    "premium": "39859"
  },
  {
    "issueNumber": "20240722010438",
    "number": "2",
    "colour": "red",
    "premium": "58382"
  },
  {
    "issueNumber": "20240722010437",
    "number": "7",
    "colour": "green",
    "premium": "35337"
  },
  {
    "issueNumber": "20240722010436",
    "number": "0",
    "colour": "red,violet",
    "premium": "44680"
  },
  {
    "issueNumber": "20240722010435",
    "number": "2",
    "colour": "red",
    "premium": "69912"
  },
  {
    "issueNumber": "20240722010434",
    "number": "9",
    "colour": "green",
    "premium": "94499"
  },
  {
    "issueNumber": "20240722010433",
    "number": "1",
    "colour": "green",
    "premium": "68451"
  },
  {
    "issueNumber": "20240722010432",
    "number": "5",
    "colour": "green,violet",
    "premium": "70055"
  },
  {
    "issueNumber": "20240722010431",
    "number": "3",
    "colour": "green",
    "premium": "66653"
  },
  {
    "issueNumber": "20240722010430",
    "number": "9",
    "colour": "green",
    "premium": "91669"
  },
  {
    "issueNumber": "20240722010429",
    "number": "9",
    "colour": "green",
    "premium": "97119"
  },
  {
    "issueNumber": "20240722010428",
    "number": "4",
    "colour": "red",
    "premium": "23524"
  },
  {
    "issueNumber": "20240722010427",
    "number": "5",
    "colour": "green,violet",
    "premium": "70475"
  },
  {
    "issueNumber": "20240722010426",
    "number": "5",
    "colour": "green,violet",
    "premium": "94955"
  },
  {
    "issueNumber": "20240722010425",
    "number": "7",
    "colour": "green",
    "premium": "40287"
  },
  {
    "issueNumber": "20240722010424",
    "number": "6",
    "colour": "red",
    "premium": "57466"
  },
  {
    "issueNumber": "20240722010423",
    "number": "7",
    "colour": "green",
    "premium": "75687"
  },
  {
    "issueNumber": "20240722010422",
    "number": "2",
    "colour": "red",
    "premium": "79512"
  },
  {
    "issueNumber": "20240722010421",
    "number": "2",
    "colour": "red",
    "premium": "56122"
  },
  {
    "issueNumber": "20240722010420",
    "number": "3",
    "colour": "green",
    "premium": "75023"
  },
  {
    "issueNumber": "20240722010419",
    "number": "7",
    "colour": "green",
    "premium": "36587"
  },
  {
    "issueNumber": "20240722010418",
    "number": "4",
    "colour": "red",
    "premium": "29024"
  },
  {
    "issueNumber": "20240722010417",
    "number": "1",
    "colour": "green",
    "premium": "38921"
  },
  {
    "issueNumber": "20240722010416",
    "number": "6",
    "colour": "red",
    "premium": "64306"
  },
  {
    "issueNumber": "20240722010415",
    "number": "3",
    "colour": "green",
    "premium": "73773"
  },
  {
    "issueNumber": "20240722010414",
    "number": "7",
    "colour": "green",
    "premium": "37327"
  },
  {
    "issueNumber": "20240722010413",
    "number": "3",
    "colour": "green",
    "premium": "39993"
  },
  {
    "issueNumber": "20240722010412",
    "number": "4",
    "colour": "red",
    "premium": "78844"
  },
  {
    "issueNumber": "20240722010411",
    "number": "2",
    "colour": "red",
    "premium": "62752"
  },
  {
    "issueNumber": "20240722010410",
    "number": "8",
    "colour": "red",
    "premium": "96818"
  },
  {
    "issueNumber": "20240722010409",
    "number": "7",
    "colour": "green",
    "premium": "17297"
  },
  {
    "issueNumber": "20240722010408",
    "number": "2",
    "colour": "red",
    "premium": "33142"
  },
  {
    "issueNumber": "20240722010407",
    "number": "5",
    "colour": "green,violet",
    "premium": "78885"
  },
  {
    "issueNumber": "20240722010406",
    "number": "8",
    "colour": "red",
    "premium": "45968"
  },
  {
    "issueNumber": "20240722010405",
    "number": "1",
    "colour": "green",
    "premium": "52731"
  },
  {
    "issueNumber": "20240722010404",
    "number": "5",
    "colour": "green,violet",
    "premium": "15505"
  },
  {
    "issueNumber": "20240722010403",
    "number": "6",
    "colour": "red",
    "premium": "46346"
  },
  {
    "issueNumber": "20240722010402",
    "number": "2",
    "colour": "red",
    "premium": "22892"
  },
  {
    "issueNumber": "20240722010401",
    "number": "5",
    "colour": "green,violet",
    "premium": "90275"
  },
  {
    "issueNumber": "20240722010400",
    "number": "2",
    "colour": "red",
    "premium": "58772"
  },
  {
    "issueNumber": "20240722010399",
    "number": "2",
    "colour": "red",
    "premium": "82812"
  },
  {
    "issueNumber": "20240722010398",
    "number": "6",
    "colour": "red",
    "premium": "61766"
  },
  {
    "issueNumber": "20240722010397",
    "number": "7",
    "colour": "green",
    "premium": "42397"
  },
  {
    "issueNumber": "20240722010396",
    "number": "1",
    "colour": "green",
    "premium": "64551"
  },
  {
    "issueNumber": "20240722010395",
    "number": "6",
    "colour": "red",
    "premium": "70906"
  },
  {
    "issueNumber": "20240722010394",
    "number": "0",
    "colour": "red,violet",
    "premium": "31780"
  },
  {
    "issueNumber": "20240722010393",
    "number": "7",
    "colour": "green",
    "premium": "41367"
  },
  {
    "issueNumber": "20240722010392",
    "number": "3",
    "colour": "green",
    "premium": "92003"
  },
  {
    "issueNumber": "20240722010391",
    "number": "3",
    "colour": "green",
    "premium": "39653"
  },
  {
    "issueNumber": "20240722010390",
    "number": "3",
    "colour": "green",
    "premium": "71633"
  },
  {
    "issueNumber": "20240722010389",
    "number": "5",
    "colour": "green,violet",
    "premium": "57215"
  },
  {
    "issueNumber": "20240722010388",
    "number": "9",
    "colour": "green",
    "premium": "71969"
  },
  {
    "issueNumber": "20240722010387",
    "number": "3",
    "colour": "green",
    "premium": "65963"
  },
  {
    "issueNumber": "20240722010386",
    "number": "0",
    "colour": "red,violet",
    "premium": "30930"
  },
  {
    "issueNumber": "20240722010385",
    "number": "1",
    "colour": "green",
    "premium": "13221"
  },
  {
    "issueNumber": "20240722010384",
    "number": "2",
    "colour": "red",
    "premium": "89272"
  },
  {
    "issueNumber": "20240722010383",
    "number": "6",
    "colour": "red",
    "premium": "28766"
  },
  {
    "issueNumber": "20240722010382",
    "number": "1",
    "colour": "green",
    "premium": "59441"
  },
  {
    "issueNumber": "20240722010381",
    "number": "2",
    "colour": "red",
    "premium": "93022"
  },
  {
    "issueNumber": "20240722010380",
    "number": "5",
    "colour": "green,violet",
    "premium": "92735"
  },
  {
    "issueNumber": "20240722010379",
    "number": "9",
    "colour": "green",
    "premium": "17589"
  },
  {
    "issueNumber": "20240722010378",
    "number": "9",
    "colour": "green",
    "premium": "18669"
  },
  {
    "issueNumber": "20240722010377",
    "number": "0",
    "colour": "red,violet",
    "premium": "55980"
  },
  {
    "issueNumber": "20240722010376",
    "number": "7",
    "colour": "green",
    "premium": "63097"
  },
  {
    "issueNumber": "20240722010375",
    "number": "3",
    "colour": "green",
    "premium": "94213"
  },
  {
    "issueNumber": "20240722010374",
    "number": "8",
    "colour": "red",
    "premium": "78048"
  },
  {
    "issueNumber": "20240722010373",
    "number": "7",
    "colour": "green",
    "premium": "69507"
  },
  {
    "issueNumber": "20240722010372",
    "number": "2",
    "colour": "red",
    "premium": "78692"
  },
  {
    "issueNumber": "20240722010371",
    "number": "6",
    "colour": "red",
    "premium": "12846"
  },
  {
    "issueNumber": "20240722010370",
    "number": "4",
    "colour": "red",
    "premium": "18484"
  },
  {
    "issueNumber": "20240722010369",
    "number": "5",
    "colour": "green,violet",
    "premium": "96865"
  },
  {
    "issueNumber": "20240722010368",
    "number": "7",
    "colour": "green",
    "premium": "21517"
  },
  {
    "issueNumber": "20240722010367",
    "number": "2",
    "colour": "red",
    "premium": "94252"
  },
  {
    "issueNumber": "20240722010366",
    "number": "7",
    "colour": "green",
    "premium": "93737"
  },
  {
    "issueNumber": "20240722010365",
    "number": "7",
    "colour": "green",
    "premium": "79827"
  },
  {
    "issueNumber": "20240722010364",
    "number": "0",
    "colour": "red,violet",
    "premium": "17970"
  },
  {
    "issueNumber": "20240722010363",
    "number": "2",
    "colour": "red",
    "premium": "24412"
  },
  {
    "issueNumber": "20240722010362",
    "number": "6",
    "colour": "red",
    "premium": "26356"
  },
  {
    "issueNumber": "20240722010361",
    "number": "8",
    "colour": "red",
    "premium": "68728"
  },
  {
    "issueNumber": "20240722010360",
    "number": "6",
    "colour": "red",
    "premium": "92456"
  },
  {
    "issueNumber": "20240722010359",
    "number": "0",
    "colour": "red,violet",
    "premium": "39500"
  },
  {
    "issueNumber": "20240722010358",
    "number": "8",
    "colour": "red",
    "premium": "49918"
  },
  {
    "issueNumber": "20240722010357",
    "number": "5",
    "colour": "green,violet",
    "premium": "16455"
  },
  {
    "issueNumber": "20240722010356",
    "number": "1",
    "colour": "green",
    "premium": "78761"
  },
  {
    "issueNumber": "20240722010355",
    "number": "3",
    "colour": "green",
    "premium": "51193"
  },
  {
    "issueNumber": "20240722010354",
    "number": "8",
    "colour": "red",
    "premium": "38308"
  },
  {
    "issueNumber": "20240722010353",
    "number": "7",
    "colour": "green",
    "premium": "53297"
  },
  {
    "issueNumber": "20240722010352",
    "number": "7",
    "colour": "green",
    "premium": "63077"
  },
  {
    "issueNumber": "20240722010351",
    "number": "2",
    "colour": "red",
    "premium": "88072"
  },
  {
    "issueNumber": "20240722010350",
    "number": "4",
    "colour": "red",
    "premium": "79554"
  },
  {
    "issueNumber": "20240722010349",
    "number": "6",
    "colour": "red",
    "premium": "25546"
  },
  {
    "issueNumber": "20240722010348",
    "number": "0",
    "colour": "red,violet",
    "premium": "24280"
  },
  {
    "issueNumber": "20240722010347",
    "number": "7",
    "colour": "green",
    "premium": "37597"
  },
  {
    "issueNumber": "20240722010346",
    "number": "2",
    "colour": "red",
    "premium": "73372"
  },
  {
    "issueNumber": "20240722010345",
    "number": "6",
    "colour": "red",
    "premium": "16026"
  },
  {
    "issueNumber": "20240722010344",
    "number": "3",
    "colour": "green",
    "premium": "59023"
  },
  {
    "issueNumber": "20240722010343",
    "number": "3",
    "colour": "green",
    "premium": "70473"
  },
  {
    "issueNumber": "20240722010342",
    "number": "9",
    "colour": "green",
    "premium": "15519"
  },
  {
    "issueNumber": "20240722010341",
    "number": "7",
    "colour": "green",
    "premium": "52597"
  },
  {
    "issueNumber": "20240722010340",
    "number": "9",
    "colour": "green",
    "premium": "64479"
  },
  {
    "issueNumber": "20240722010339",
    "number": "2",
    "colour": "red",
    "premium": "85052"
  },
  {
    "issueNumber": "20240722010338",
    "number": "4",
    "colour": "red",
    "premium": "80084"
  },
  {
    "issueNumber": "20240722010337",
    "number": "7",
    "colour": "green",
    "premium": "55267"
  },
  {
    "issueNumber": "20240722010336",
    "number": "7",
    "colour": "green",
    "premium": "53077"
  },
  {
    "issueNumber": "20240722010335",
    "number": "0",
    "colour": "red,violet",
    "premium": "90200"
  },
  {
    "issueNumber": "20240722010334",
    "number": "5",
    "colour": "green,violet",
    "premium": "64725"
  },
  {
    "issueNumber": "20240722010333",
    "number": "3",
    "colour": "green",
    "premium": "55403"
  },
  {
    "issueNumber": "20240722010332",
    "number": "1",
    "colour": "green",
    "premium": "86631"
  },
  {
    "issueNumber": "20240722010331",
    "number": "5",
    "colour": "green,violet",
    "premium": "82935"
  },
  {
    "issueNumber": "20240722010330",
    "number": "4",
    "colour": "red",
    "premium": "87354"
  },
  {
    "issueNumber": "20240722010329",
    "number": "9",
    "colour": "green",
    "premium": "67329"
  },
  {
    "issueNumber": "20240722010328",
    "number": "5",
    "colour": "green,violet",
    "premium": "58985"
  },
  {
    "issueNumber": "20240722010327",
    "number": "1",
    "colour": "green",
    "premium": "26141"
  },
  {
    "issueNumber": "20240722010326",
    "number": "0",
    "colour": "red,violet",
    "premium": "35450"
  },
  {
    "issueNumber": "20240722010325",
    "number": "3",
    "colour": "green",
    "premium": "72083"
  },
  {
    "issueNumber": "20240722010324",
    "number": "2",
    "colour": "red",
    "premium": "44122"
  },
  {
    "issueNumber": "20240722010323",
    "number": "1",
    "colour": "green",
    "premium": "72661"
  },
  {
    "issueNumber": "20240722010322",
    "number": "7",
    "colour": "green",
    "premium": "76517"
  },
  {
    "issueNumber": "20240722010321",
    "number": "1",
    "colour": "green",
    "premium": "36361"
  },
  {
    "issueNumber": "20240722010320",
    "number": "8",
    "colour": "red",
    "premium": "88248"
  },
  {
    "issueNumber": "20240722010319",
    "number": "2",
    "colour": "red",
    "premium": "84442"
  },
  {
    "issueNumber": "20240722010318",
    "number": "3",
    "colour": "green",
    "premium": "24673"
  },
  {
    "issueNumber": "20240722010317",
    "number": "5",
    "colour": "green,violet",
    "premium": "70985"
  },
  {
    "issueNumber": "20240722010316",
    "number": "6",
    "colour": "red",
    "premium": "22336"
  },
  {
    "issueNumber": "20240722010315",
    "number": "6",
    "colour": "red",
    "premium": "44416"
  },
  {
    "issueNumber": "20240722010314",
    "number": "0",
    "colour": "red,violet",
    "premium": "87340"
  },
  {
    "issueNumber": "20240722010313",
    "number": "7",
    "colour": "green",
    "premium": "32637"
  },
  {
    "issueNumber": "20240722010312",
    "number": "4",
    "colour": "red",
    "premium": "35914"
  },
  {
    "issueNumber": "20240722010311",
    "number": "0",
    "colour": "red,violet",
    "premium": "13900"
  },
  {
    "issueNumber": "20240722010310",
    "number": "3",
    "colour": "green",
    "premium": "75033"
  },
  {
    "issueNumber": "20240722010309",
    "number": "8",
    "colour": "red",
    "premium": "82388"
  },
  {
    "issueNumber": "20240722010308",
    "number": "5",
    "colour": "green,violet",
    "premium": "46935"
  },
  {
    "issueNumber": "20240722010307",
    "number": "8",
    "colour": "red",
    "premium": "70088"
  },
  {
    "issueNumber": "20240722010306",
    "number": "8",
    "colour": "red",
    "premium": "49878"
  },
  {
    "issueNumber": "20240722010305",
    "number": "7",
    "colour": "green",
    "premium": "62057"
  },
  {
    "issueNumber": "20240722010304",
    "number": "4",
    "colour": "red",
    "premium": "21904"
  },
  {
    "issueNumber": "20240722010303",
    "number": "2",
    "colour": "red",
    "premium": "18762"
  },
  {
    "issueNumber": "20240722010302",
    "number": "4",
    "colour": "red",
    "premium": "44784"
  },
  {
    "issueNumber": "20240722010301",
    "number": "4",
    "colour": "red",
    "premium": "52964"
  },
  {
    "issueNumber": "20240722010300",
    "number": "2",
    "colour": "red",
    "premium": "83252"
  },
  {
    "issueNumber": "20240722010299",
    "number": "1",
    "colour": "green",
    "premium": "39311"
  },
  {
    "issueNumber": "20240722010298",
    "number": "1",
    "colour": "green",
    "premium": "61821"
  },
  {
    "issueNumber": "20240722010297",
    "number": "9",
    "colour": "green",
    "premium": "30719"
  },
  {
    "issueNumber": "20240722010296",
    "number": "5",
    "colour": "green,violet",
    "premium": "86535"
  },
  {
    "issueNumber": "20240722010295",
    "number": "6",
    "colour": "red",
    "premium": "46326"
  },
  {
    "issueNumber": "20240722010294",
    "number": "7",
    "colour": "green",
    "premium": "75107"
  },
  {
    "issueNumber": "20240722010293",
    "number": "5",
    "colour": "green,violet",
    "premium": "17885"
  },
  {
    "issueNumber": "20240722010292",
    "number": "4",
    "colour": "red",
    "premium": "28934"
  },
  {
    "issueNumber": "20240722010291",
    "number": "2",
    "colour": "red",
    "premium": "67022"
  },
  {
    "issueNumber": "20240722010290",
    "number": "6",
    "colour": "red",
    "premium": "95916"
  },
  {
    "issueNumber": "20240722010289",
    "number": "5",
    "colour": "green,violet",
    "premium": "74215"
  },
  {
    "issueNumber": "20240722010288",
    "number": "7",
    "colour": "green",
    "premium": "62067"
  },
  {
    "issueNumber": "20240722010287",
    "number": "5",
    "colour": "green,violet",
    "premium": "15805"
  },
  {
    "issueNumber": "20240722010286",
    "number": "8",
    "colour": "red",
    "premium": "73158"
  },
  {
    "issueNumber": "20240722010285",
    "number": "3",
    "colour": "green",
    "premium": "99083"
  },
  {
    "issueNumber": "20240722010284",
    "number": "5",
    "colour": "green,violet",
    "premium": "39505"
  },
  {
    "issueNumber": "20240722010283",
    "number": "7",
    "colour": "green",
    "premium": "46397"
  },
  {
    "issueNumber": "20240722010282",
    "number": "1",
    "colour": "green",
    "premium": "78401"
  },
  {
    "issueNumber": "20240722010281",
    "number": "8",
    "colour": "red",
    "premium": "68588"
  },
  {
    "issueNumber": "20240722010280",
    "number": "3",
    "colour": "green",
    "premium": "61853"
  },
  {
    "issueNumber": "20240722010279",
    "number": "1",
    "colour": "green",
    "premium": "69171"
  },
  {
    "issueNumber": "20240722010278",
    "number": "3",
    "colour": "green",
    "premium": "39883"
  },
  {
    "issueNumber": "20240722010277",
    "number": "9",
    "colour": "green",
    "premium": "96979"
  },
  {
    "issueNumber": "20240722010276",
    "number": "1",
    "colour": "green",
    "premium": "62811"
  },
  {
    "issueNumber": "20240722010275",
    "number": "3",
    "colour": "green",
    "premium": "91283"
  },
  {
    "issueNumber": "20240722010274",
    "number": "7",
    "colour": "green",
    "premium": "64097"
  },
  {
    "issueNumber": "20240722010273",
    "number": "3",
    "colour": "green",
    "premium": "24463"
  },
  {
    "issueNumber": "20240722010272",
    "number": "7",
    "colour": "green",
    "premium": "77237"
  },
  {
    "issueNumber": "20240722010271",
    "number": "0",
    "colour": "red,violet",
    "premium": "96580"
  },
  {
    "issueNumber": "20240722010270",
    "number": "6",
    "colour": "red",
    "premium": "46256"
  },
  {
    "issueNumber": "20240722010269",
    "number": "1",
    "colour": "green",
    "premium": "82071"
  },
  {
    "issueNumber": "20240722010268",
    "number": "5",
    "colour": "green,violet",
    "premium": "20335"
  },
  {
    "issueNumber": "20240722010267",
    "number": "1",
    "colour": "green",
    "premium": "20571"
  },
  {
    "issueNumber": "20240722010266",
    "number": "0",
    "colour": "red,violet",
    "premium": "82800"
  },
  {
    "issueNumber": "20240722010265",
    "number": "9",
    "colour": "green",
    "premium": "69289"
  },
  {
    "issueNumber": "20240722010264",
    "number": "7",
    "colour": "green",
    "premium": "96237"
  },
  {
    "issueNumber": "20240722010263",
    "number": "8",
    "colour": "red",
    "premium": "62348"
  },
  {
    "issueNumber": "20240722010262",
    "number": "7",
    "colour": "green",
    "premium": "65337"
  },
  {
    "issueNumber": "20240722010261",
    "number": "5",
    "colour": "green,violet",
    "premium": "40865"
  },
  {
    "issueNumber": "20240722010260",
    "number": "7",
    "colour": "green",
    "premium": "43667"
  },
  {
    "issueNumber": "20240722010259",
    "number": "4",
    "colour": "red",
    "premium": "86004"
  },
  {
    "issueNumber": "20240722010258",
    "number": "4",
    "colour": "red",
    "premium": "93174"
  },
  {
    "issueNumber": "20240722010257",
    "number": "6",
    "colour": "red",
    "premium": "31296"
  },
  {
    "issueNumber": "20240722010256",
    "number": "5",
    "colour": "green,violet",
    "premium": "94525"
  },
  {
    "issueNumber": "20240722010255",
    "number": "2",
    "colour": "red",
    "premium": "12412"
  },
  {
    "issueNumber": "20240722010254",
    "number": "8",
    "colour": "red",
    "premium": "70858"
  },
  {
    "issueNumber": "20240722010253",
    "number": "1",
    "colour": "green",
    "premium": "41801"
  },
  {
    "issueNumber": "20240722010252",
    "number": "2",
    "colour": "red",
    "premium": "47022"
  },
  {
    "issueNumber": "20240722010251",
    "number": "4",
    "colour": "red",
    "premium": "17424"
  },
  {
    "issueNumber": "20240722010250",
    "number": "7",
    "colour": "green",
    "premium": "36247"
  },
  {
    "issueNumber": "20240722010249",
    "number": "5",
    "colour": "green,violet",
    "premium": "20955"
  },
  {
    "issueNumber": "20240722010248",
    "number": "0",
    "colour": "red,violet",
    "premium": "19930"
  },
  {
    "issueNumber": "20240722010247",
    "number": "8",
    "colour": "red",
    "premium": "90968"
  },
  {
    "issueNumber": "20240722010246",
    "number": "7",
    "colour": "green",
    "premium": "19067"
  },
  {
    "issueNumber": "20240722010245",
    "number": "7",
    "colour": "green",
    "premium": "80667"
  },
  {
    "issueNumber": "20240722010244",
    "number": "7",
    "colour": "green",
    "premium": "45177"
  },
  {
    "issueNumber": "20240722010243",
    "number": "8",
    "colour": "red",
    "premium": "23968"
  },
  {
    "issueNumber": "20240722010242",
    "number": "9",
    "colour": "green",
    "premium": "69859"
  },
  {
    "issueNumber": "20240722010241",
    "number": "6",
    "colour": "red",
    "premium": "60386"
  },
  {
    "issueNumber": "20240722010240",
    "number": "8",
    "colour": "red",
    "premium": "22318"
  },
  {
    "issueNumber": "20240722010239",
    "number": "0",
    "colour": "red,violet",
    "premium": "82580"
  },
  {
    "issueNumber": "20240722010238",
    "number": "0",
    "colour": "red,violet",
    "premium": "43830"
  },
  {
    "issueNumber": "20240722010237",
    "number": "8",
    "colour": "red",
    "premium": "39818"
  },
  {
    "issueNumber": "20240722010236",
    "number": "2",
    "colour": "red",
    "premium": "44732"
  },
  {
    "issueNumber": "20240722010235",
    "number": "7",
    "colour": "green",
    "premium": "41227"
  },
  {
    "issueNumber": "20240722010234",
    "number": "3",
    "colour": "green",
    "premium": "49423"
  },
  {
    "issueNumber": "20240722010233",
    "number": "4",
    "colour": "red",
    "premium": "16284"
  },
  {
    "issueNumber": "20240722010232",
    "number": "7",
    "colour": "green",
    "premium": "33497"
  },
  {
    "issueNumber": "20240722010231",
    "number": "6",
    "colour": "red",
    "premium": "23416"
  },
  {
    "issueNumber": "20240722010230",
    "number": "3",
    "colour": "green",
    "premium": "95673"
  },
  {
    "issueNumber": "20240722010229",
    "number": "3",
    "colour": "green",
    "premium": "77963"
  },
  {
    "issueNumber": "20240722010228",
    "number": "3",
    "colour": "green",
    "premium": "64443"
  },
  {
    "issueNumber": "20240722010227",
    "number": "2",
    "colour": "red",
    "premium": "35052"
  },
  {
    "issueNumber": "20240722010226",
    "number": "0",
    "colour": "red,violet",
    "premium": "68910"
  },
  {
    "issueNumber": "20240722010225",
    "number": "4",
    "colour": "red",
    "premium": "13294"
  },
  {
    "issueNumber": "20240722010224",
    "number": "2",
    "colour": "red",
    "premium": "75562"
  },
  {
    "issueNumber": "20240722010223",
    "number": "0",
    "colour": "red,violet",
    "premium": "52400"
  },
  {
    "issueNumber": "20240722010222",
    "number": "4",
    "colour": "red",
    "premium": "39194"
  },
  {
    "issueNumber": "20240722010221",
    "number": "3",
    "colour": "green",
    "premium": "79353"
  },
  {
    "issueNumber": "20240722010220",
    "number": "2",
    "colour": "red",
    "premium": "78172"
  },
  {
    "issueNumber": "20240722010219",
    "number": "7",
    "colour": "green",
    "premium": "33927"
  },
  {
    "issueNumber": "20240722010218",
    "number": "6",
    "colour": "red",
    "premium": "48586"
  },
  {
    "issueNumber": "20240722010217",
    "number": "6",
    "colour": "red",
    "premium": "96416"
  },
  {
    "issueNumber": "20240722010216",
    "number": "5",
    "colour": "green,violet",
    "premium": "54685"
  },
  {
    "issueNumber": "20240722010215",
    "number": "8",
    "colour": "red",
    "premium": "61608"
  },
  {
    "issueNumber": "20240722010214",
    "number": "7",
    "colour": "green",
    "premium": "96567"
  },
  {
    "issueNumber": "20240722010213",
    "number": "7",
    "colour": "green",
    "premium": "16337"
  },
  {
    "issueNumber": "20240722010212",
    "number": "7",
    "colour": "green",
    "premium": "61287"
  },
  {
    "issueNumber": "20240722010211",
    "number": "3",
    "colour": "green",
    "premium": "23583"
  },
  {
    "issueNumber": "20240722010210",
    "number": "0",
    "colour": "red,violet",
    "premium": "56950"
  },
  {
    "issueNumber": "20240722010209",
    "number": "9",
    "colour": "green",
    "premium": "56119"
  },
  {
    "issueNumber": "20240722010208",
    "number": "7",
    "colour": "green",
    "premium": "51977"
  },
  {
    "issueNumber": "20240722010207",
    "number": "4",
    "colour": "red",
    "premium": "80214"
  },
  {
    "issueNumber": "20240722010206",
    "number": "6",
    "colour": "red",
    "premium": "89166"
  },
  {
    "issueNumber": "20240722010205",
    "number": "0",
    "colour": "red,violet",
    "premium": "77680"
  },
  {
    "issueNumber": "20240722010204",
    "number": "4",
    "colour": "red",
    "premium": "97004"
  },
  {
    "issueNumber": "20240722010203",
    "number": "7",
    "colour": "green",
    "premium": "94327"
  },
  {
    "issueNumber": "20240722010202",
    "number": "7",
    "colour": "green",
    "premium": "96857"
  },
  {
    "issueNumber": "20240722010201",
    "number": "0",
    "colour": "red,violet",
    "premium": "97080"
  },
  {
    "issueNumber": "20240722010200",
    "number": "6",
    "colour": "red",
    "premium": "89396"
  },
  {
    "issueNumber": "20240722010199",
    "number": "3",
    "colour": "green",
    "premium": "22093"
  },
  {
    "issueNumber": "20240722010198",
    "number": "2",
    "colour": "red",
    "premium": "53322"
  },
  {
    "issueNumber": "20240722010197",
    "number": "1",
    "colour": "green",
    "premium": "58751"
  },
  {
    "issueNumber": "20240722010196",
    "number": "4",
    "colour": "red",
    "premium": "23824"
  },
  {
    "issueNumber": "20240722010195",
    "number": "9",
    "colour": "green",
    "premium": "80219"
  },
  {
    "issueNumber": "20240722010194",
    "number": "7",
    "colour": "green",
    "premium": "75857"
  },
  {
    "issueNumber": "20240722010193",
    "number": "1",
    "colour": "green",
    "premium": "12731"
  },
  {
    "issueNumber": "20240722010192",
    "number": "9",
    "colour": "green",
    "premium": "70869"
  },
  {
    "issueNumber": "20240722010191",
    "number": "9",
    "colour": "green",
    "premium": "88049"
  },
  {
    "issueNumber": "20240722010190",
    "number": "6",
    "colour": "red",
    "premium": "53856"
  },
  {
    "issueNumber": "20240722010189",
    "number": "4",
    "colour": "red",
    "premium": "51124"
  },
  {
    "issueNumber": "20240722010188",
    "number": "4",
    "colour": "red",
    "premium": "87704"
  },
  {
    "issueNumber": "20240722010187",
    "number": "2",
    "colour": "red",
    "premium": "26592"
  },
  {
    "issueNumber": "20240722010186",
    "number": "0",
    "colour": "red,violet",
    "premium": "64920"
  },
  {
    "issueNumber": "20240722010185",
    "number": "4",
    "colour": "red",
    "premium": "84204"
  },
  {
    "issueNumber": "20240722010184",
    "number": "4",
    "colour": "red",
    "premium": "38344"
  },
  {
    "issueNumber": "20240722010183",
    "number": "5",
    "colour": "green,violet",
    "premium": "31355"
  },
  {
    "issueNumber": "20240722010182",
    "number": "1",
    "colour": "green",
    "premium": "95631"
  },
  {
    "issueNumber": "20240722010181",
    "number": "5",
    "colour": "green,violet",
    "premium": "90165"
  },
  {
    "issueNumber": "20240722010180",
    "number": "3",
    "colour": "green",
    "premium": "40943"
  },
  {
    "issueNumber": "20240722010179",
    "number": "2",
    "colour": "red",
    "premium": "19302"
  },
  {
    "issueNumber": "20240722010178",
    "number": "9",
    "colour": "green",
    "premium": "20809"
  },
  {
    "issueNumber": "20240722010177",
    "number": "0",
    "colour": "red,violet",
    "premium": "53710"
  },
  {
    "issueNumber": "20240722010176",
    "number": "8",
    "colour": "red",
    "premium": "92438"
  },
  {
    "issueNumber": "20240722010175",
    "number": "2",
    "colour": "red",
    "premium": "47892"
  },
  {
    "issueNumber": "20240722010174",
    "number": "7",
    "colour": "green",
    "premium": "55047"
  },
  {
    "issueNumber": "20240722010173",
    "number": "9",
    "colour": "green",
    "premium": "83159"
  },
  {
    "issueNumber": "20240722010172",
    "number": "0",
    "colour": "red,violet",
    "premium": "31420"
  },
  {
    "issueNumber": "20240722010171",
    "number": "8",
    "colour": "red",
    "premium": "42828"
  },
  {
    "issueNumber": "20240722010170",
    "number": "0",
    "colour": "red,violet",
    "premium": "65650"
  },
  {
    "issueNumber": "20240722010169",
    "number": "6",
    "colour": "red",
    "premium": "16386"
  },
  {
    "issueNumber": "20240722010168",
    "number": "7",
    "colour": "green",
    "premium": "32007"
  },
  {
    "issueNumber": "20240722010167",
    "number": "8",
    "colour": "red",
    "premium": "54458"
  },
  {
    "issueNumber": "20240722010166",
    "number": "9",
    "colour": "green",
    "premium": "70709"
  },
  {
    "issueNumber": "20240722010165",
    "number": "6",
    "colour": "red",
    "premium": "82206"
  },
  {
    "issueNumber": "20240722010164",
    "number": "8",
    "colour": "red",
    "premium": "55898"
  },
  {
    "issueNumber": "20240722010163",
    "number": "6",
    "colour": "red",
    "premium": "18956"
  },
  {
    "issueNumber": "20240722010162",
    "number": "2",
    "colour": "red",
    "premium": "70222"
  },
  {
    "issueNumber": "20240722010161",
    "number": "6",
    "colour": "red",
    "premium": "68786"
  },
  {
    "issueNumber": "20240722010160",
    "number": "1",
    "colour": "green",
    "premium": "70071"
  },
  {
    "issueNumber": "20240722010159",
    "number": "1",
    "colour": "green",
    "premium": "12241"
  },
  {
    "issueNumber": "20240722010158",
    "number": "0",
    "colour": "red,violet",
    "premium": "58260"
  },
  {
    "issueNumber": "20240722010157",
    "number": "4",
    "colour": "red",
    "premium": "20934"
  },
  {
    "issueNumber": "20240722010156",
    "number": "1",
    "colour": "green",
    "premium": "56381"
  },
  {
    "issueNumber": "20240722010155",
    "number": "3",
    "colour": "green",
    "premium": "94443"
  },
  {
    "issueNumber": "20240722010154",
    "number": "3",
    "colour": "green",
    "premium": "86623"
  },
  {
    "issueNumber": "20240722010153",
    "number": "8",
    "colour": "red",
    "premium": "33748"
  },
  {
    "issueNumber": "20240722010152",
    "number": "5",
    "colour": "green,violet",
    "premium": "50935"
  },
  {
    "issueNumber": "20240722010151",
    "number": "3",
    "colour": "green",
    "premium": "30093"
  },
  {
    "issueNumber": "20240722010150",
    "number": "6",
    "colour": "red",
    "premium": "82996"
  },
  {
    "issueNumber": "20240722010149",
    "number": "9",
    "colour": "green",
    "premium": "25899"
  },
  {
    "issueNumber": "20240722010148",
    "number": "9",
    "colour": "green",
    "premium": "40369"
  },
  {
    "issueNumber": "20240722010147",
    "number": "9",
    "colour": "green",
    "premium": "47479"
  },
  {
    "issueNumber": "20240722010146",
    "number": "6",
    "colour": "red",
    "premium": "64346"
  },
  {
    "issueNumber": "20240722010145",
    "number": "3",
    "colour": "green",
    "premium": "45473"
  },
  {
    "issueNumber": "20240722010144",
    "number": "8",
    "colour": "red",
    "premium": "61408"
  },
  {
    "issueNumber": "20240722010143",
    "number": "4",
    "colour": "red",
    "premium": "17714"
  },
  {
    "issueNumber": "20240722010142",
    "number": "4",
    "colour": "red",
    "premium": "10044"
  },
  {
    "issueNumber": "20240722010141",
    "number": "1",
    "colour": "green",
    "premium": "52401"
  },
  {
    "issueNumber": "20240722010140",
    "number": "7",
    "colour": "green",
    "premium": "63287"
  },
  {
    "issueNumber": "20240722010139",
    "number": "8",
    "colour": "red",
    "premium": "97638"
  },
  {
    "issueNumber": "20240722010138",
    "number": "3",
    "colour": "green",
    "premium": "51733"
  },
  {
    "issueNumber": "20240722010137",
    "number": "8",
    "colour": "red",
    "premium": "93748"
  },
  {
    "issueNumber": "20240722010136",
    "number": "9",
    "colour": "green",
    "premium": "30529"
  },
  {
    "issueNumber": "20240722010135",
    "number": "6",
    "colour": "red",
    "premium": "97116"
  },
  {
    "issueNumber": "20240722010134",
    "number": "1",
    "colour": "green",
    "premium": "97181"
  },
  {
    "issueNumber": "20240722010133",
    "number": "8",
    "colour": "red",
    "premium": "72008"
  },
  {
    "issueNumber": "20240722010132",
    "number": "7",
    "colour": "green",
    "premium": "19737"
  },
  {
    "issueNumber": "20240722010131",
    "number": "3",
    "colour": "green",
    "premium": "29443"
  },
  {
    "issueNumber": "20240722010130",
    "number": "4",
    "colour": "red",
    "premium": "51924"
  },
  {
    "issueNumber": "20240722010129",
    "number": "6",
    "colour": "red",
    "premium": "53046"
  },
  {
    "issueNumber": "20240722010128",
    "number": "7",
    "colour": "green",
    "premium": "38777"
  },
  {
    "issueNumber": "20240722010127",
    "number": "3",
    "colour": "green",
    "premium": "96033"
  },
  {
    "issueNumber": "20240722010126",
    "number": "2",
    "colour": "red",
    "premium": "41402"
  },
  {
    "issueNumber": "20240722010125",
    "number": "5",
    "colour": "green,violet",
    "premium": "16595"
  },
  {
    "issueNumber": "20240722010124",
    "number": "4",
    "colour": "red",
    "premium": "80484"
  },
  {
    "issueNumber": "20240722010123",
    "number": "4",
    "colour": "red",
    "premium": "90514"
  },
  {
    "issueNumber": "20240722010122",
    "number": "2",
    "colour": "red",
    "premium": "18442"
  },
  {
    "issueNumber": "20240722010121",
    "number": "2",
    "colour": "red",
    "premium": "21932"
  },
  {
    "issueNumber": "20240722010120",
    "number": "3",
    "colour": "green",
    "premium": "19493"
  },
  {
    "issueNumber": "20240722010119",
    "number": "2",
    "colour": "red",
    "premium": "92642"
  },
  {
    "issueNumber": "20240722010118",
    "number": "9",
    "colour": "green",
    "premium": "19209"
  },
  {
    "issueNumber": "20240722010117",
    "number": "8",
    "colour": "red",
    "premium": "29278"
  },
  {
    "issueNumber": "20240722010116",
    "number": "6",
    "colour": "red",
    "premium": "70526"
  },
  {
    "issueNumber": "20240722010115",
    "number": "3",
    "colour": "green",
    "premium": "66813"
  },
  {
    "issueNumber": "20240722010114",
    "number": "6",
    "colour": "red",
    "premium": "40396"
  },
  {
    "issueNumber": "20240722010113",
    "number": "2",
    "colour": "red",
    "premium": "39502"
  },
  {
    "issueNumber": "20240722010112",
    "number": "0",
    "colour": "red,violet",
    "premium": "56150"
  },
  {
    "issueNumber": "20240722010111",
    "number": "5",
    "colour": "green,violet",
    "premium": "59225"
  },
  {
    "issueNumber": "20240722010110",
    "number": "0",
    "colour": "red,violet",
    "premium": "69600"
  },
  {
    "issueNumber": "20240722010109",
    "number": "4",
    "colour": "red",
    "premium": "94524"
  },
  {
    "issueNumber": "20240722010108",
    "number": "2",
    "colour": "red",
    "premium": "81302"
  },
  {
    "issueNumber": "20240722010107",
    "number": "9",
    "colour": "green",
    "premium": "26879"
  },
  {
    "issueNumber": "20240722010106",
    "number": "8",
    "colour": "red",
    "premium": "86748"
  },
  {
    "issueNumber": "20240722010105",
    "number": "4",
    "colour": "red",
    "premium": "69784"
  },
  {
    "issueNumber": "20240722010104",
    "number": "6",
    "colour": "red",
    "premium": "63246"
  },
  {
    "issueNumber": "20240722010103",
    "number": "3",
    "colour": "green",
    "premium": "61643"
  },
  {
    "issueNumber": "20240722010102",
    "number": "6",
    "colour": "red",
    "premium": "28746"
  },
  {
    "issueNumber": "20240722010101",
    "number": "0",
    "colour": "red,violet",
    "premium": "81140"
  },
  {
    "issueNumber": "20240722010100",
    "number": "2",
    "colour": "red",
    "premium": "82922"
  },
  {
    "issueNumber": "20240722010099",
    "number": "8",
    "colour": "red",
    "premium": "11888"
  },
  {
    "issueNumber": "20240722010098",
    "number": "1",
    "colour": "green",
    "premium": "64611"
  },
  {
    "issueNumber": "20240722010097",
    "number": "2",
    "colour": "red",
    "premium": "10542"
  },
  {
    "issueNumber": "20240722010096",
    "number": "9",
    "colour": "green",
    "premium": "55039"
  },
  {
    "issueNumber": "20240722010095",
    "number": "2",
    "colour": "red",
    "premium": "54442"
  },
  {
    "issueNumber": "20240722010094",
    "number": "8",
    "colour": "red",
    "premium": "85218"
  },
  {
    "issueNumber": "20240722010093",
    "number": "7",
    "colour": "green",
    "premium": "15737"
  },
  {
    "issueNumber": "20240722010092",
    "number": "9",
    "colour": "green",
    "premium": "81359"
  },
  {
    "issueNumber": "20240722010091",
    "number": "2",
    "colour": "red",
    "premium": "83102"
  },
  {
    "issueNumber": "20240722010090",
    "number": "0",
    "colour": "red,violet",
    "premium": "44210"
  },
  {
    "issueNumber": "20240722010089",
    "number": "1",
    "colour": "green",
    "premium": "24931"
  },
  {
    "issueNumber": "20240722010088",
    "number": "4",
    "colour": "red",
    "premium": "60234"
  },
  {
    "issueNumber": "20240722010087",
    "number": "1",
    "colour": "green",
    "premium": "48941"
  },
  {
    "issueNumber": "20240722010086",
    "number": "8",
    "colour": "red",
    "premium": "57198"
  },
  {
    "issueNumber": "20240722010085",
    "number": "8",
    "colour": "red",
    "premium": "13638"
  },
  {
    "issueNumber": "20240722010084",
    "number": "8",
    "colour": "red",
    "premium": "63818"
  },
  {
    "issueNumber": "20240722010083",
    "number": "4",
    "colour": "red",
    "premium": "56024"
  },
  {
    "issueNumber": "20240722010082",
    "number": "3",
    "colour": "green",
    "premium": "23333"
  },
  {
    "issueNumber": "20240722010081",
    "number": "0",
    "colour": "red,violet",
    "premium": "45380"
  },
  {
    "issueNumber": "20240722010080",
    "number": "0",
    "colour": "red,violet",
    "premium": "87080"
  },
  {
    "issueNumber": "20240722010079",
    "number": "3",
    "colour": "green",
    "premium": "62143"
  },
  {
    "issueNumber": "20240722010078",
    "number": "1",
    "colour": "green",
    "premium": "38451"
  },
  {
    "issueNumber": "20240722010077",
    "number": "8",
    "colour": "red",
    "premium": "11258"
  },
  {
    "issueNumber": "20240722010076",
    "number": "9",
    "colour": "green",
    "premium": "99669"
  },
  {
    "issueNumber": "20240722010075",
    "number": "2",
    "colour": "red",
    "premium": "68372"
  },
  {
    "issueNumber": "20240722010074",
    "number": "8",
    "colour": "red",
    "premium": "91878"
  },
  {
    "issueNumber": "20240722010073",
    "number": "3",
    "colour": "green",
    "premium": "68203"
  },
  {
    "issueNumber": "20240722010072",
    "number": "4",
    "colour": "red",
    "premium": "85244"
  },
  {
    "issueNumber": "20240722010071",
    "number": "0",
    "colour": "red,violet",
    "premium": "80200"
  },
  {
    "issueNumber": "20240722010070",
    "number": "9",
    "colour": "green",
    "premium": "27229"
  },
  {
    "issueNumber": "20240722010069",
    "number": "2",
    "colour": "red",
    "premium": "41642"
  },
  {
    "issueNumber": "20240722010068",
    "number": "7",
    "colour": "green",
    "premium": "44707"
  },
  {
    "issueNumber": "20240722010067",
    "number": "0",
    "colour": "red,violet",
    "premium": "18970"
  },
  {
    "issueNumber": "20240722010066",
    "number": "7",
    "colour": "green",
    "premium": "37907"
  },
  {
    "issueNumber": "20240722010065",
    "number": "0",
    "colour": "red,violet",
    "premium": "34890"
  },
  {
    "issueNumber": "20240722010064",
    "number": "5",
    "colour": "green,violet",
    "premium": "98475"
  },
  {
    "issueNumber": "20240722010063",
    "number": "5",
    "colour": "green,violet",
    "premium": "56525"
  },
  {
    "issueNumber": "20240722010062",
    "number": "7",
    "colour": "green",
    "premium": "40797"
  },
  {
    "issueNumber": "20240722010061",
    "number": "6",
    "colour": "red",
    "premium": "49686"
  },
  {
    "issueNumber": "20240722010060",
    "number": "7",
    "colour": "green",
    "premium": "65227"
  },
  {
    "issueNumber": "20240722010059",
    "number": "8",
    "colour": "red",
    "premium": "36978"
  },
  {
    "issueNumber": "20240722010058",
    "number": "0",
    "colour": "red,violet",
    "premium": "29510"
  },
  {
    "issueNumber": "20240722010057",
    "number": "6",
    "colour": "red",
    "premium": "53706"
  },
  {
    "issueNumber": "20240722010056",
    "number": "9",
    "colour": "green",
    "premium": "23779"
  },
  {
    "issueNumber": "20240722010055",
    "number": "6",
    "colour": "red",
    "premium": "19606"
  },
  {
    "issueNumber": "20240722010054",
    "number": "3",
    "colour": "green",
    "premium": "51073"
  },
  {
    "issueNumber": "20240722010053",
    "number": "1",
    "colour": "green",
    "premium": "13671"
  },
  {
    "issueNumber": "20240722010052",
    "number": "5",
    "colour": "green,violet",
    "premium": "35025"
  },
  {
    "issueNumber": "20240722010051",
    "number": "7",
    "colour": "green",
    "premium": "25677"
  },
  {
    "issueNumber": "20240722010050",
    "number": "9",
    "colour": "green",
    "premium": "13199"
  },
  {
    "issueNumber": "20240722010049",
    "number": "3",
    "colour": "green",
    "premium": "67193"
  },
  {
    "issueNumber": "20240722010048",
    "number": "1",
    "colour": "green",
    "premium": "53271"
  },
  {
    "issueNumber": "20240722010047",
    "number": "5",
    "colour": "green,violet",
    "premium": "18115"
  },
  {
    "issueNumber": "20240722010046",
    "number": "6",
    "colour": "red",
    "premium": "90546"
  },
  {
    "issueNumber": "20240722010045",
    "number": "1",
    "colour": "green",
    "premium": "14341"
  },
  {
    "issueNumber": "20240722010044",
    "number": "7",
    "colour": "green",
    "premium": "36747"
  },
  {
    "issueNumber": "20240722010043",
    "number": "3",
    "colour": "green",
    "premium": "31243"
  },
  {
    "issueNumber": "20240722010042",
    "number": "5",
    "colour": "green,violet",
    "premium": "22425"
  },
  {
    "issueNumber": "20240722010041",
    "number": "6",
    "colour": "red",
    "premium": "24976"
  },
  {
    "issueNumber": "20240722010040",
    "number": "3",
    "colour": "green",
    "premium": "45143"
  },
  {
    "issueNumber": "20240722010039",
    "number": "3",
    "colour": "green",
    "premium": "52943"
  },
  {
    "issueNumber": "20240722010038",
    "number": "1",
    "colour": "green",
    "premium": "49771"
  },
  {
    "issueNumber": "20240722010037",
    "number": "4",
    "colour": "red",
    "premium": "69014"
  },
  {
    "issueNumber": "20240722010036",
    "number": "7",
    "colour": "green",
    "premium": "14997"
  },
  {
    "issueNumber": "20240722010035",
    "number": "5",
    "colour": "green,violet",
    "premium": "26545"
  },
  {
    "issueNumber": "20240722010034",
    "number": "5",
    "colour": "green,violet",
    "premium": "16195"
  },
  {
    "issueNumber": "20240722010033",
    "number": "8",
    "colour": "red",
    "premium": "62078"
  },
  {
    "issueNumber": "20240722010032",
    "number": "3",
    "colour": "green",
    "premium": "73553"
  },
  {
    "issueNumber": "20240722010031",
    "number": "9",
    "colour": "green",
    "premium": "86619"
  },
  {
    "issueNumber": "20240722010030",
    "number": "4",
    "colour": "red",
    "premium": "66484"
  },
  {
    "issueNumber": "20240722010029",
    "number": "0",
    "colour": "red,violet",
    "premium": "22120"
  },
  {
    "issueNumber": "20240722010028",
    "number": "0",
    "colour": "red,violet",
    "premium": "79350"
  },
  {
    "issueNumber": "20240722010027",
    "number": "3",
    "colour": "green",
    "premium": "65643"
  },
  {
    "issueNumber": "20240722010026",
    "number": "1",
    "colour": "green",
    "premium": "70641"
  },
  {
    "issueNumber": "20240722010025",
    "number": "5",
    "colour": "green,violet",
    "premium": "53375"
  },
  {
    "issueNumber": "20240722010024",
    "number": "9",
    "colour": "green",
    "premium": "71869"
  },
  {
    "issueNumber": "20240722010023",
    "number": "1",
    "colour": "green",
    "premium": "59001"
  },
  {
    "issueNumber": "20240722010022",
    "number": "8",
    "colour": "red",
    "premium": "10798"
  },
  {
    "issueNumber": "20240722010021",
    "number": "2",
    "colour": "red",
    "premium": "89052"
  },
  {
    "issueNumber": "20240722010020",
    "number": "3",
    "colour": "green",
    "premium": "52583"
  },
  {
    "issueNumber": "20240722010019",
    "number": "2",
    "colour": "red",
    "premium": "15622"
  },
  {
    "issueNumber": "20240722010018",
    "number": "8",
    "colour": "red",
    "premium": "24988"
  },
  {
    "issueNumber": "20240722010017",
    "number": "3",
    "colour": "green",
    "premium": "84863"
  },
  {
    "issueNumber": "20240722010016",
    "number": "1",
    "colour": "green",
    "premium": "18381"
  },
  {
    "issueNumber": "20240722010015",
    "number": "5",
    "colour": "green,violet",
    "premium": "31215"
  },
  {
    "issueNumber": "20240722010014",
    "number": "4",
    "colour": "red",
    "premium": "14684"
  },
  {
    "issueNumber": "20240722010013",
    "number": "2",
    "colour": "red",
    "premium": "29662"
  },
  {
    "issueNumber": "20240722010012",
    "number": "5",
    "colour": "green,violet",
    "premium": "49765"
  },
  {
    "issueNumber": "20240722010011",
    "number": "4",
    "colour": "red",
    "premium": "64544"
  },
  {
    "issueNumber": "20240722010010",
    "number": "7",
    "colour": "green",
    "premium": "29327"
  },
  {
    "issueNumber": "20240722010009",
    "number": "0",
    "colour": "red,violet",
    "premium": "80180"
  },
  {
    "issueNumber": "20240722010008",
    "number": "9",
    "colour": "green",
    "premium": "50699"
  },
  {
    "issueNumber": "20240722010007",
    "number": "4",
    "colour": "red",
    "premium": "69854"
  },
  {
    "issueNumber": "20240722010006",
    "number": "7",
    "colour": "green",
    "premium": "79797"
  },
  {
    "issueNumber": "20240722010005",
    "number": "0",
    "colour": "red,violet",
    "premium": "26010"
  },
  {
    "issueNumber": "20240722010004",
    "number": "5",
    "colour": "green,violet",
    "premium": "79715"
  },
  {
    "issueNumber": "20240722010003",
    "number": "5",
    "colour": "green,violet",
    "premium": "69785"
  },
  {
    "issueNumber": "20240722010002",
    "number": "1",
    "colour": "green",
    "premium": "56891"
  },
  {
    "issueNumber": "20240722010001",
    "number": "9",
    "colour": "green",
    "premium": "57579"
  },
  {
    "issueNumber": "20240721011440",
    "number": "2",
    "colour": "red",
    "premium": "39242"
  },
  {
    "issueNumber": "20240721011439",
    "number": "5",
    "colour": "green,violet",
    "premium": "69705"
  },
  {
    "issueNumber": "20240721011438",
    "number": "9",
    "colour": "green",
    "premium": "71999"
  },
  {
    "issueNumber": "20240721011437",
    "number": "7",
    "colour": "green",
    "premium": "73857"
  },
  {
    "issueNumber": "20240721011436",
    "number": "9",
    "colour": "green",
    "premium": "43339"
  },
  {
    "issueNumber": "20240721011435",
    "number": "9",
    "colour": "green",
    "premium": "49009"
  },
  {
    "issueNumber": "20240721011434",
    "number": "7",
    "colour": "green",
    "premium": "72047"
  },
  {
    "issueNumber": "20240721011433",
    "number": "8",
    "colour": "red",
    "premium": "34868"
  },
  {
    "issueNumber": "20240721011432",
    "number": "0",
    "colour": "red,violet",
    "premium": "35700"
  },
  {
    "issueNumber": "20240721011431",
    "number": "2",
    "colour": "red",
    "premium": "17162"
  },
  {
    "issueNumber": "20240721011430",
    "number": "3",
    "colour": "green",
    "premium": "72723"
  },
  {
    "issueNumber": "20240721011429",
    "number": "7",
    "colour": "green",
    "premium": "81977"
  },
  {
    "issueNumber": "20240721011428",
    "number": "1",
    "colour": "green",
    "premium": "79831"
  },
  {
    "issueNumber": "20240721011427",
    "number": "7",
    "colour": "green",
    "premium": "27867"
  },
  {
    "issueNumber": "20240721011426",
    "number": "5",
    "colour": "green,violet",
    "premium": "85065"
  },
  {
    "issueNumber": "20240721011425",
    "number": "1",
    "colour": "green",
    "premium": "37451"
  },
  {
    "issueNumber": "20240721011424",
    "number": "3",
    "colour": "green",
    "premium": "96753"
  },
  {
    "issueNumber": "20240721011423",
    "number": "0",
    "colour": "red,violet",
    "premium": "94880"
  },
  {
    "issueNumber": "20240721011422",
    "number": "8",
    "colour": "red",
    "premium": "33968"
  },
  {
    "issueNumber": "20240721011421",
    "number": "3",
    "colour": "green",
    "premium": "13813"
  },
  {
    "issueNumber": "20240721011420",
    "number": "1",
    "colour": "green",
    "premium": "95331"
  },
  {
    "issueNumber": "20240721011419",
    "number": "3",
    "colour": "green",
    "premium": "11353"
  },
  {
    "issueNumber": "20240721011418",
    "number": "9",
    "colour": "green",
    "premium": "86699"
  },
  {
    "issueNumber": "20240721011417",
    "number": "6",
    "colour": "red",
    "premium": "37576"
  },
  {
    "issueNumber": "20240721011416",
    "number": "7",
    "colour": "green",
    "premium": "23597"
  },
  {
    "issueNumber": "20240721011415",
    "number": "7",
    "colour": "green",
    "premium": "52907"
  },
  {
    "issueNumber": "20240721011414",
    "number": "9",
    "colour": "green",
    "premium": "74049"
  },
  {
    "issueNumber": "20240721011413",
    "number": "5",
    "colour": "green,violet",
    "premium": "51705"
  },
  {
    "issueNumber": "20240721011412",
    "number": "2",
    "colour": "red",
    "premium": "88192"
  },
  {
    "issueNumber": "20240721011411",
    "number": "9",
    "colour": "green",
    "premium": "83019"
  },
  {
    "issueNumber": "20240721011410",
    "number": "1",
    "colour": "green",
    "premium": "70661"
  },
  {
    "issueNumber": "20240721011409",
    "number": "0",
    "colour": "red,violet",
    "premium": "10340"
  },
  {
    "issueNumber": "20240721011408",
    "number": "4",
    "colour": "red",
    "premium": "93044"
  },
  {
    "issueNumber": "20240721011407",
    "number": "0",
    "colour": "red,violet",
    "premium": "98890"
  },
  {
    "issueNumber": "20240721011406",
    "number": "0",
    "colour": "red,violet",
    "premium": "97600"
  },
  {
    "issueNumber": "20240721011405",
    "number": "2",
    "colour": "red",
    "premium": "50462"
  },
  {
    "issueNumber": "20240721011404",
    "number": "0",
    "colour": "red,violet",
    "premium": "11920"
  },
  {
    "issueNumber": "20240721011403",
    "number": "2",
    "colour": "red",
    "premium": "19372"
  },
  {
    "issueNumber": "20240721011402",
    "number": "3",
    "colour": "green",
    "premium": "36983"
  },
  {
    "issueNumber": "20240721011401",
    "number": "2",
    "colour": "red",
    "premium": "78032"
  },
  {
    "issueNumber": "20240721011400",
    "number": "9",
    "colour": "green",
    "premium": "31149"
  },
  {
    "issueNumber": "20240721011399",
    "number": "0",
    "colour": "red,violet",
    "premium": "93280"
  },
  {
    "issueNumber": "20240721011398",
    "number": "6",
    "colour": "red",
    "premium": "38816"
  },
  {
    "issueNumber": "20240721011397",
    "number": "0",
    "colour": "red,violet",
    "premium": "70950"
  },
  {
    "issueNumber": "20240721011396",
    "number": "4",
    "colour": "red",
    "premium": "27794"
  },
  {
    "issueNumber": "20240721011395",
    "number": "4",
    "colour": "red",
    "premium": "89314"
  },
  {
    "issueNumber": "20240721011394",
    "number": "4",
    "colour": "red",
    "premium": "50404"
  },
  {
    "issueNumber": "20240721011393",
    "number": "6",
    "colour": "red",
    "premium": "79086"
  },
  {
    "issueNumber": "20240721011392",
    "number": "3",
    "colour": "green",
    "premium": "87253"
  },
  {
    "issueNumber": "20240721011391",
    "number": "1",
    "colour": "green",
    "premium": "27741"
  },
  {
    "issueNumber": "20240721011390",
    "number": "5",
    "colour": "green,violet",
    "premium": "70925"
  },
  {
    "issueNumber": "20240721011389",
    "number": "2",
    "colour": "red",
    "premium": "37742"
  },
  {
    "issueNumber": "20240721011388",
    "number": "3",
    "colour": "green",
    "premium": "63963"
  },
  {
    "issueNumber": "20240721011387",
    "number": "7",
    "colour": "green",
    "premium": "63947"
  },
  {
    "issueNumber": "20240721011386",
    "number": "5",
    "colour": "green,violet",
    "premium": "51385"
  },
  {
    "issueNumber": "20240721011385",
    "number": "1",
    "colour": "green",
    "premium": "93781"
  },
  {
    "issueNumber": "20240721011384",
    "number": "2",
    "colour": "red",
    "premium": "60692"
  },
  {
    "issueNumber": "20240721011383",
    "number": "2",
    "colour": "red",
    "premium": "53982"
  },
  {
    "issueNumber": "20240721011382",
    "number": "7",
    "colour": "green",
    "premium": "64497"
  },
  {
    "issueNumber": "20240721011381",
    "number": "8",
    "colour": "red",
    "premium": "86968"
  },
  {
    "issueNumber": "20240721011380",
    "number": "5",
    "colour": "green,violet",
    "premium": "49605"
  },
  {
    "issueNumber": "20240721011379",
    "number": "2",
    "colour": "red",
    "premium": "25252"
  },
  {
    "issueNumber": "20240721011378",
    "number": "9",
    "colour": "green",
    "premium": "37229"
  },
  {
    "issueNumber": "20240721011377",
    "number": "4",
    "colour": "red",
    "premium": "32374"
  },
  {
    "issueNumber": "20240721011376",
    "number": "4",
    "colour": "red",
    "premium": "22054"
  },
  {
    "issueNumber": "20240721011375",
    "number": "3",
    "colour": "green",
    "premium": "19493"
  },
  {
    "issueNumber": "20240721011374",
    "number": "1",
    "colour": "green",
    "premium": "99851"
  },
  {
    "issueNumber": "20240721011373",
    "number": "0",
    "colour": "red,violet",
    "premium": "54940"
  },
  {
    "issueNumber": "20240721011372",
    "number": "4",
    "colour": "red",
    "premium": "59494"
  },
  {
    "issueNumber": "20240721011371",
    "number": "6",
    "colour": "red",
    "premium": "19126"
  },
  {
    "issueNumber": "20240721011370",
    "number": "1",
    "colour": "green",
    "premium": "21011"
  },
  {
    "issueNumber": "20240721011369",
    "number": "6",
    "colour": "red",
    "premium": "75566"
  },
  {
    "issueNumber": "20240721011368",
    "number": "2",
    "colour": "red",
    "premium": "49322"
  },
  {
    "issueNumber": "20240721011367",
    "number": "3",
    "colour": "green",
    "premium": "97903"
  },
  {
    "issueNumber": "20240721011366",
    "number": "8",
    "colour": "red",
    "premium": "54578"
  },
  {
    "issueNumber": "20240721011365",
    "number": "4",
    "colour": "red",
    "premium": "11654"
  },
  {
    "issueNumber": "20240721011364",
    "number": "5",
    "colour": "green,violet",
    "premium": "39315"
  },
  {
    "issueNumber": "20240721011363",
    "number": "8",
    "colour": "red",
    "premium": "24208"
  },
  {
    "issueNumber": "20240721011362",
    "number": "4",
    "colour": "red",
    "premium": "71284"
  },
  {
    "issueNumber": "20240721011361",
    "number": "8",
    "colour": "red",
    "premium": "60288"
  },
  {
    "issueNumber": "20240721011360",
    "number": "1",
    "colour": "green",
    "premium": "55781"
  },
  {
    "issueNumber": "20240721011359",
    "number": "2",
    "colour": "red",
    "premium": "83462"
  },
  {
    "issueNumber": "20240721011358",
    "number": "4",
    "colour": "red",
    "premium": "15364"
  },
  {
    "issueNumber": "20240721011357",
    "number": "3",
    "colour": "green",
    "premium": "86503"
  },
  {
    "issueNumber": "20240721011356",
    "number": "0",
    "colour": "red,violet",
    "premium": "81620"
  },
  {
    "issueNumber": "20240721011355",
    "number": "8",
    "colour": "red",
    "premium": "75158"
  },
  {
    "issueNumber": "20240721011354",
    "number": "9",
    "colour": "green",
    "premium": "79089"
  },
  {
    "issueNumber": "20240721011353",
    "number": "2",
    "colour": "red",
    "premium": "45982"
  },
  {
    "issueNumber": "20240721011352",
    "number": "0",
    "colour": "red,violet",
    "premium": "14420"
  },
  {
    "issueNumber": "20240721011351",
    "number": "4",
    "colour": "red",
    "premium": "19334"
  },
  {
    "issueNumber": "20240721011350",
    "number": "2",
    "colour": "red",
    "premium": "73402"
  },
  {
    "issueNumber": "20240721011349",
    "number": "4",
    "colour": "red",
    "premium": "28124"
  },
  {
    "issueNumber": "20240721011348",
    "number": "7",
    "colour": "green",
    "premium": "97737"
  },
  {
    "issueNumber": "20240721011347",
    "number": "7",
    "colour": "green",
    "premium": "61797"
  },
  {
    "issueNumber": "20240721011346",
    "number": "8",
    "colour": "red",
    "premium": "67798"
  },
  {
    "issueNumber": "20240721011345",
    "number": "6",
    "colour": "red",
    "premium": "40366"
  },
  {
    "issueNumber": "20240721011344",
    "number": "2",
    "colour": "red",
    "premium": "32722"
  },
  {
    "issueNumber": "20240721011343",
    "number": "7",
    "colour": "green",
    "premium": "44127"
  },
  {
    "issueNumber": "20240721011342",
    "number": "4",
    "colour": "red",
    "premium": "63864"
  },
  {
    "issueNumber": "20240721011341",
    "number": "5",
    "colour": "green,violet",
    "premium": "77215"
  },
  {
    "issueNumber": "20240721011340",
    "number": "7",
    "colour": "green",
    "premium": "45417"
  },
  {
    "issueNumber": "20240721011339",
    "number": "0",
    "colour": "red,violet",
    "premium": "93560"
  },
  {
    "issueNumber": "20240721011338",
    "number": "1",
    "colour": "green",
    "premium": "98761"
  },
  {
    "issueNumber": "20240721011337",
    "number": "6",
    "colour": "red",
    "premium": "13306"
  },
  {
    "issueNumber": "20240721011336",
    "number": "5",
    "colour": "green,violet",
    "premium": "98265"
  },
  {
    "issueNumber": "20240721011335",
    "number": "3",
    "colour": "green",
    "premium": "71713"
  },
  {
    "issueNumber": "20240721011334",
    "number": "8",
    "colour": "red",
    "premium": "60518"
  },
  {
    "issueNumber": "20240721011333",
    "number": "6",
    "colour": "red",
    "premium": "11076"
  },
  {
    "issueNumber": "20240721011332",
    "number": "0",
    "colour": "red,violet",
    "premium": "29670"
  },
  {
    "issueNumber": "20240721011331",
    "number": "4",
    "colour": "red",
    "premium": "24154"
  },
  {
    "issueNumber": "20240721011330",
    "number": "8",
    "colour": "red",
    "premium": "26098"
  },
  {
    "issueNumber": "20240721011329",
    "number": "5",
    "colour": "green,violet",
    "premium": "54565"
  },
  {
    "issueNumber": "20240721011328",
    "number": "6",
    "colour": "red",
    "premium": "31236"
  },
  {
    "issueNumber": "20240721011327",
    "number": "6",
    "colour": "red",
    "premium": "13156"
  },
  {
    "issueNumber": "20240721011326",
    "number": "7",
    "colour": "green",
    "premium": "76327"
  },
  {
    "issueNumber": "20240721011325",
    "number": "6",
    "colour": "red",
    "premium": "78666"
  },
  {
    "issueNumber": "20240721011324",
    "number": "0",
    "colour": "red,violet",
    "premium": "88220"
  },
  {
    "issueNumber": "20240721011323",
    "number": "4",
    "colour": "red",
    "premium": "95114"
  },
  {
    "issueNumber": "20240721011322",
    "number": "7",
    "colour": "green",
    "premium": "21227"
  },
  {
    "issueNumber": "20240721011321",
    "number": "7",
    "colour": "green",
    "premium": "71817"
  },
  {
    "issueNumber": "20240721011320",
    "number": "5",
    "colour": "green,violet",
    "premium": "67835"
  },
  {
    "issueNumber": "20240721011319",
    "number": "7",
    "colour": "green",
    "premium": "59567"
  },
  {
    "issueNumber": "20240721011318",
    "number": "8",
    "colour": "red",
    "premium": "32438"
  },
  {
    "issueNumber": "20240721011317",
    "number": "4",
    "colour": "red",
    "premium": "26674"
  },
  {
    "issueNumber": "20240721011316",
    "number": "9",
    "colour": "green",
    "premium": "23669"
  },
  {
    "issueNumber": "20240721011315",
    "number": "4",
    "colour": "red",
    "premium": "99004"
  },
  {
    "issueNumber": "20240721011314",
    "number": "8",
    "colour": "red",
    "premium": "18548"
  },
  {
    "issueNumber": "20240721011313",
    "number": "0",
    "colour": "red,violet",
    "premium": "13360"
  },
  {
    "issueNumber": "20240721011312",
    "number": "4",
    "colour": "red",
    "premium": "13034"
  },
  {
    "issueNumber": "20240721011311",
    "number": "9",
    "colour": "green",
    "premium": "66169"
  },
  {
    "issueNumber": "20240721011310",
    "number": "9",
    "colour": "green",
    "premium": "90729"
  },
  {
    "issueNumber": "20240721011309",
    "number": "2",
    "colour": "red",
    "premium": "23412"
  },
  {
    "issueNumber": "20240721011308",
    "number": "3",
    "colour": "green",
    "premium": "66073"
  },
  {
    "issueNumber": "20240721011307",
    "number": "6",
    "colour": "red",
    "premium": "54286"
  },
  {
    "issueNumber": "20240721011306",
    "number": "4",
    "colour": "red",
    "premium": "68874"
  },
  {
    "issueNumber": "20240721011305",
    "number": "1",
    "colour": "green",
    "premium": "60091"
  },
  {
    "issueNumber": "20240721011304",
    "number": "4",
    "colour": "red",
    "premium": "98634"
  },
  {
    "issueNumber": "20240721011303",
    "number": "7",
    "colour": "green",
    "premium": "24447"
  },
  {
    "issueNumber": "20240721011302",
    "number": "2",
    "colour": "red",
    "premium": "64132"
  },
  {
    "issueNumber": "20240721011301",
    "number": "5",
    "colour": "green,violet",
    "premium": "24455"
  },
  {
    "issueNumber": "20240721011300",
    "number": "4",
    "colour": "red",
    "premium": "64154"
  },
  {
    "issueNumber": "20240721011299",
    "number": "6",
    "colour": "red",
    "premium": "84016"
  },
  {
    "issueNumber": "20240721011298",
    "number": "1",
    "colour": "green",
    "premium": "90601"
  },
  {
    "issueNumber": "20240721011297",
    "number": "9",
    "colour": "green",
    "premium": "65849"
  },
  {
    "issueNumber": "20240721011296",
    "number": "0",
    "colour": "red,violet",
    "premium": "21790"
  },
  {
    "issueNumber": "20240721011295",
    "number": "9",
    "colour": "green",
    "premium": "68889"
  },
  {
    "issueNumber": "20240721011294",
    "number": "3",
    "colour": "green",
    "premium": "36203"
  },
  {
    "issueNumber": "20240721011293",
    "number": "4",
    "colour": "red",
    "premium": "33754"
  },
  {
    "issueNumber": "20240721011292",
    "number": "9",
    "colour": "green",
    "premium": "70129"
  },
  {
    "issueNumber": "20240721011291",
    "number": "4",
    "colour": "red",
    "premium": "15134"
  },
  {
    "issueNumber": "20240721011290",
    "number": "1",
    "colour": "green",
    "premium": "81101"
  },
  {
    "issueNumber": "20240721011289",
    "number": "9",
    "colour": "green",
    "premium": "13469"
  },
  {
    "issueNumber": "20240721011288",
    "number": "9",
    "colour": "green",
    "premium": "59989"
  },
  {
    "issueNumber": "20240721011287",
    "number": "8",
    "colour": "red",
    "premium": "90018"
  },
  {
    "issueNumber": "20240721011286",
    "number": "6",
    "colour": "red",
    "premium": "75906"
  },
  {
    "issueNumber": "20240721011285",
    "number": "5",
    "colour": "green,violet",
    "premium": "41395"
  },
  {
    "issueNumber": "20240721011284",
    "number": "9",
    "colour": "green",
    "premium": "32509"
  },
  {
    "issueNumber": "20240721011283",
    "number": "1",
    "colour": "green",
    "premium": "27151"
  },
  {
    "issueNumber": "20240721011282",
    "number": "6",
    "colour": "red",
    "premium": "61666"
  },
  {
    "issueNumber": "20240721011281",
    "number": "1",
    "colour": "green",
    "premium": "27411"
  },
  {
    "issueNumber": "20240721011280",
    "number": "5",
    "colour": "green,violet",
    "premium": "38985"
  },
  {
    "issueNumber": "20240721011279",
    "number": "7",
    "colour": "green",
    "premium": "40407"
  },
  {
    "issueNumber": "20240721011278",
    "number": "6",
    "colour": "red",
    "premium": "76396"
  },
  {
    "issueNumber": "20240721011277",
    "number": "7",
    "colour": "green",
    "premium": "32837"
  },
  {
    "issueNumber": "20240721011276",
    "number": "0",
    "colour": "red,violet",
    "premium": "23340"
  },
  {
    "issueNumber": "20240721011275",
    "number": "5",
    "colour": "green,violet",
    "premium": "38905"
  },
  {
    "issueNumber": "20240721011274",
    "number": "0",
    "colour": "red,violet",
    "premium": "83420"
  },
  {
    "issueNumber": "20240721011273",
    "number": "8",
    "colour": "red",
    "premium": "11538"
  },
  {
    "issueNumber": "20240721011272",
    "number": "7",
    "colour": "green",
    "premium": "43717"
  },
  {
    "issueNumber": "20240721011271",
    "number": "9",
    "colour": "green",
    "premium": "38589"
  },
  {
    "issueNumber": "20240721011270",
    "number": "4",
    "colour": "red",
    "premium": "54734"
  },
  {
    "issueNumber": "20240721011269",
    "number": "7",
    "colour": "green",
    "premium": "90637"
  },
  {
    "issueNumber": "20240721011268",
    "number": "0",
    "colour": "red,violet",
    "premium": "26220"
  },
  {
    "issueNumber": "20240721011267",
    "number": "4",
    "colour": "red",
    "premium": "53834"
  },
  {
    "issueNumber": "20240721011266",
    "number": "8",
    "colour": "red",
    "premium": "29248"
  },
  {
    "issueNumber": "20240721011265",
    "number": "1",
    "colour": "green",
    "premium": "54451"
  },
  {
    "issueNumber": "20240721011264",
    "number": "9",
    "colour": "green",
    "premium": "91659"
  },
  {
    "issueNumber": "20240721011263",
    "number": "6",
    "colour": "red",
    "premium": "24016"
  },
  {
    "issueNumber": "20240721011262",
    "number": "7",
    "colour": "green",
    "premium": "85317"
  },
  {
    "issueNumber": "20240721011261",
    "number": "6",
    "colour": "red",
    "premium": "93926"
  },
  {
    "issueNumber": "20240721011260",
    "number": "8",
    "colour": "red",
    "premium": "62218"
  },
  {
    "issueNumber": "20240721011259",
    "number": "2",
    "colour": "red",
    "premium": "53322"
  },
  {
    "issueNumber": "20240721011258",
    "number": "2",
    "colour": "red",
    "premium": "76002"
  },
  {
    "issueNumber": "20240721011257",
    "number": "5",
    "colour": "green,violet",
    "premium": "13635"
  },
  {
    "issueNumber": "20240721011256",
    "number": "9",
    "colour": "green",
    "premium": "96049"
  },
  {
    "issueNumber": "20240721011255",
    "number": "8",
    "colour": "red",
    "premium": "65798"
  },
  {
    "issueNumber": "20240721011254",
    "number": "4",
    "colour": "red",
    "premium": "93774"
  },
  {
    "issueNumber": "20240721011253",
    "number": "2",
    "colour": "red",
    "premium": "93012"
  },
  {
    "issueNumber": "20240721011252",
    "number": "3",
    "colour": "green",
    "premium": "96263"
  },
  {
    "issueNumber": "20240721011251",
    "number": "6",
    "colour": "red",
    "premium": "44556"
  },
  {
    "issueNumber": "20240721011250",
    "number": "2",
    "colour": "red",
    "premium": "78132"
  },
  {
    "issueNumber": "20240721011249",
    "number": "9",
    "colour": "green",
    "premium": "21919"
  },
  {
    "issueNumber": "20240721011248",
    "number": "8",
    "colour": "red",
    "premium": "68478"
  },
  {
    "issueNumber": "20240721011247",
    "number": "8",
    "colour": "red",
    "premium": "85898"
  },
  {
    "issueNumber": "20240721011246",
    "number": "1",
    "colour": "green",
    "premium": "72541"
  },
  {
    "issueNumber": "20240721011245",
    "number": "6",
    "colour": "red",
    "premium": "25706"
  },
  {
    "issueNumber": "20240721011244",
    "number": "2",
    "colour": "red",
    "premium": "38972"
  },
  {
    "issueNumber": "20240721011243",
    "number": "3",
    "colour": "green",
    "premium": "89753"
  },
  {
    "issueNumber": "20240721011242",
    "number": "0",
    "colour": "red,violet",
    "premium": "73390"
  },
  {
    "issueNumber": "20240721011241",
    "number": "8",
    "colour": "red",
    "premium": "31328"
  },
  {
    "issueNumber": "20240721011240",
    "number": "2",
    "colour": "red",
    "premium": "81632"
  },
  {
    "issueNumber": "20240721011239",
    "number": "2",
    "colour": "red",
    "premium": "49662"
  },
  {
    "issueNumber": "20240721011238",
    "number": "0",
    "colour": "red,violet",
    "premium": "38630"
  },
  {
    "issueNumber": "20240721011237",
    "number": "6",
    "colour": "red",
    "premium": "19756"
  },
  {
    "issueNumber": "20240721011236",
    "number": "1",
    "colour": "green",
    "premium": "93261"
  },
  {
    "issueNumber": "20240721011235",
    "number": "0",
    "colour": "red,violet",
    "premium": "20920"
  },
  {
    "issueNumber": "20240721011234",
    "number": "6",
    "colour": "red",
    "premium": "16646"
  },
  {
    "issueNumber": "20240721011233",
    "number": "5",
    "colour": "green,violet",
    "premium": "54675"
  },
  {
    "issueNumber": "20240721011232",
    "number": "0",
    "colour": "red,violet",
    "premium": "12540"
  },
  {
    "issueNumber": "20240721011231",
    "number": "9",
    "colour": "green",
    "premium": "44719"
  },
  {
    "issueNumber": "20240721011230",
    "number": "2",
    "colour": "red",
    "premium": "84762"
  },
  {
    "issueNumber": "20240721011229",
    "number": "6",
    "colour": "red",
    "premium": "26496"
  },
  {
    "issueNumber": "20240721011228",
    "number": "8",
    "colour": "red",
    "premium": "48648"
  },
  {
    "issueNumber": "20240721011227",
    "number": "8",
    "colour": "red",
    "premium": "70298"
  },
  {
    "issueNumber": "20240721011226",
    "number": "6",
    "colour": "red",
    "premium": "82136"
  },
  {
    "issueNumber": "20240721011225",
    "number": "4",
    "colour": "red",
    "premium": "13764"
  },
  {
    "issueNumber": "20240721011224",
    "number": "5",
    "colour": "green,violet",
    "premium": "94715"
  },
  {
    "issueNumber": "20240721011223",
    "number": "5",
    "colour": "green,violet",
    "premium": "38525"
  },
  {
    "issueNumber": "20240721011222",
    "number": "2",
    "colour": "red",
    "premium": "52172"
  },
  {
    "issueNumber": "20240721011221",
    "number": "6",
    "colour": "red",
    "premium": "56896"
  },
  {
    "issueNumber": "20240721011220",
    "number": "5",
    "colour": "green,violet",
    "premium": "79475"
  },
  {
    "issueNumber": "20240721011219",
    "number": "5",
    "colour": "green,violet",
    "premium": "94925"
  },
  {
    "issueNumber": "20240721011218",
    "number": "5",
    "colour": "green,violet",
    "premium": "83715"
  },
  {
    "issueNumber": "20240721011217",
    "number": "4",
    "colour": "red",
    "premium": "30044"
  },
  {
    "issueNumber": "20240721011216",
    "number": "3",
    "colour": "green",
    "premium": "67003"
  },
  {
    "issueNumber": "20240721011215",
    "number": "6",
    "colour": "red",
    "premium": "13516"
  },
  {
    "issueNumber": "20240721011214",
    "number": "0",
    "colour": "red,violet",
    "premium": "83840"
  },
  {
    "issueNumber": "20240721011213",
    "number": "6",
    "colour": "red",
    "premium": "64246"
  },
  {
    "issueNumber": "20240721011212",
    "number": "5",
    "colour": "green,violet",
    "premium": "89265"
  },
  {
    "issueNumber": "20240721011211",
    "number": "8",
    "colour": "red",
    "premium": "51618"
  },
  {
    "issueNumber": "20240721011210",
    "number": "2",
    "colour": "red",
    "premium": "38752"
  },
  {
    "issueNumber": "20240721011209",
    "number": "6",
    "colour": "red",
    "premium": "65266"
  },
  {
    "issueNumber": "20240721011208",
    "number": "4",
    "colour": "red",
    "premium": "81354"
  },
  {
    "issueNumber": "20240721011207",
    "number": "6",
    "colour": "red",
    "premium": "31576"
  },
  {
    "issueNumber": "20240721011206",
    "number": "0",
    "colour": "red,violet",
    "premium": "95630"
  },
  {
    "issueNumber": "20240721011205",
    "number": "0",
    "colour": "red,violet",
    "premium": "97630"
  },
  {
    "issueNumber": "20240721011204",
    "number": "6",
    "colour": "red",
    "premium": "82016"
  },
  {
    "issueNumber": "20240721011203",
    "number": "4",
    "colour": "red",
    "premium": "92124"
  },
  {
    "issueNumber": "20240721011202",
    "number": "4",
    "colour": "red",
    "premium": "53624"
  },
  {
    "issueNumber": "20240721011201",
    "number": "0",
    "colour": "red,violet",
    "premium": "87280"
  }
]
# Determine color and size based on the number
def determine_color_and_size(number):
    number = int(number)
    color = 'red' if number % 2 == 0 else 'green'
    size = 'small' if number <= 4 else 'big'
    return color, size

# Sort data by issueNumber
sorted_data = sorted(data, key=lambda x: int(x['issueNumber']))

# Add color and size to each entry
for entry in sorted_data:
    color, size = determine_color_and_size(entry['number'])
    entry['color'] = color
    entry['size'] = size

# Filter data to ensure only consecutive issue numbers
consecutive_data = []
previous_issue = None
for entry in sorted_data:
    current_issue = int(entry['issueNumber'])
    if previous_issue is None or current_issue == previous_issue + 1:
        consecutive_data.append(entry)
        previous_issue = current_issue

# Function to detect trends
def detect_trends(data):
    trends = {'increase': [], 'decrease': []}
    previous_premium = None
    for entry in data:
        current_premium = int(entry['premium'])
        if previous_premium is None:
            previous_premium = current_premium
            continue

        if current_premium > previous_premium:
            trends['increase'].append(entry)
        elif current_premium < previous_premium:
            trends['decrease'].append(entry)
        
        previous_premium = current_premium
    
    return trends

# Group data by color and size
grouped_data = {}
for entry in consecutive_data:
    key = f"{entry['color']}_{entry['size']}"
    if key not in grouped_data:
        grouped_data[key] = []
    grouped_data[key].append(entry)

# Detect trends for each group
trends = {key: detect_trends(entries) for key, entries in grouped_data.items()}

# Function to filter data by issueNumber range
def filter_by_issue_number(data, start_suffix, end_suffix):
    filtered_data = []
    for entry in data:
        issue_suffix = int(entry['issueNumber'][-4:])
        if start_suffix <= issue_suffix <= end_suffix:
            filtered_data.append(entry)
    return filtered_data

# Filter data for issue numbers from 0001 to the current maximum suffix
start_suffix = 1
end_suffix = int(consecutive_data[-1]['issueNumber'][-4:])
filtered_data = filter_by_issue_number(consecutive_data, start_suffix, end_suffix)

# Print the results
print("Filtered Data by Issue Number Suffix:")
for entry in filtered_data:
    print(entry)

print("\nDetected Trends:")
for key, trend_data in trends.items():
    print(f"Group: {key}")
    print("Increasing Trends:")
    for trend in trend_data['increase']:
        print(trend)
    print("Decreasing Trends:")
    for trend in trend_data['decrease']:
        print(trend)

# Function to predict next round movement
def predict_next_movement(data):
    if not data:
        return None

    last_entry = data[-1]
    last_number = int(last_entry['number'])
    next_number = (last_number + 1) % 10
    color, size = determine_color_and_size(next_number)
    return {'predicted_color': color, 'predicted_size': size, 'next_number': next_number}

# Predict the next round movement
next_movement = predict_next_movement(consecutive_data)
print("\nPredicted Next Round Movement:")
print(next_movement)
