# def get_username():
#     user_name = "bhandariayush_"
#     return user_name
#
#
# def get_api(user_name):
#     return "https://www.instagram.com/{0}/?__a=1".format(user_name)
import requests

from insta_profile import InstaProfile
#diff
list_username = [
    "minionish_1994",
    "nvnainaverma",
    "komaldegwekar",
    "aasif.jamadar",
    "anuj.salsa",
    "shashwat_mishra3",
    "kunal_sahani14",
    "mike.2331",
    "charvi_chouhan",
    "diyadutta",
    "hitesh.auji",
    "azizadegwekar",
    "kimberlyd98",
    "figment_of_the_universe",
    "poorvakarnik",
    "shwetaskul",
    "houseofdarbouka_",
    "abhidnya_pawar",
    "nirajpardeshi",
    "pranavpardeshi",
    "samhita_adc",
    "adc.madhurima",
    "adc.akram",
    "sahsahil",
    "sagarrathore123",
    "_harshali_1415",
    "bhagya_st",
    "x_ru_sh_ab_x",
    "rushi_rich1",
    "mr_r_a_j_p_u_t_2019",
    "deepikatikoo",
    "21_tej_12",
    "pramoddancerdp",
    "_suiya_",
    "sweta_fernandes_",
    "pouravi_patwardhan",
    "radhikamehta_",
    "dishamulik1",
    "juileed",
    "kasturikarandikar",
    "rising_star_aniket",
    "ianuprita",
    "ipoojapawar",
    "chica_tootsie",
    "apurval95",
    "tannushreerakshit",
    "unnikriishnan",
    "either_hungry_or_sleepy",
    "prernakhoda",
    "nishkamble",
    "shubhshitole123",
    "zin_prince_",
    "surve_sayali",
    "tahitisenguptadutta",
    "harshit.rungta",
    "leena_patle",
    "shreyachauhan1526",
    "suraj_dancemachine",
    "choreographer_satish",
    "namit_chhajed",
    "pune_dance_fitness",
    "akshaygrms",
    "abhi_isiwaqt",
    "goag7",
    "gokhale.archana",
    "rahul_theswagcrew",
    "moze_sushant",
    "dancingdevilpawan",
    "dancingdevil_komal",
    "rasikas_art_studio_official",
    "ritikajoybox",
    "navtaalgarba2622",
    "radhikapatil140890",
    "mehul.khimavat",
    "_m_u_g_d_h_a",
    "manasikanetkar",
    "nitikeshgaikwadbpcindia",
    "suraj_beatpopper_01",
    "shubh191",
    "priyanka_sonya",
    "sushil_keskar__24",
    "hiren_swcpune",
    "pareshadmane",
    "ajinkyasinghbansi_",
    "tttejaaallll",
    "swarali_umesh1111",
    "dancewithtrupti",
    "dance_addictor",
    "lady_praj",
    "prakashsatya19",
    "pranjal_17_kothari",
    "shelarpravin87",
    "sajan.rajpurohit.58",
    "murumkarrahul",
    "poojapb_artistree",
    "karpepurva551",
    "priyapashankar",
    "rishikaysh_desae",
    "anjalikukreja",
    "rahulindulkar",
    "punam4dance",
    "sushmita_thedancingsoul",
    "kartikiiii__ ",
    "dikshalankeshwar",
    "asha_ponikiewska",
    "iamvishaltelang",
    "arunbhardwaj_official",
    "bajaj.tanvi",
    "ms.sayli",
    "akshay_bhosle1",
    "priyankasonya",
    "theamritayadav",
    "sandeep_shivashankar",
    "zinnishi7557",
    "kalyani.choudhari",
    "poojalokhande5",
    "nikitaraja2014",
    "suresh_dahale",
    "punam_majee",
    "shubham_lokhande000",
    "shashikumar_shetty_999",
    "i.am.satyakisaha",
    "surabhiparikh",
    "rutuja.rode",
    "vipuldevrani",
    "himali__walkoli",

    "nimitkotian",
    "aki_nikhs",
    "ajit_insideme",
    "ravivarma.iam",

    "suraj_9721",
    "virengiri_",
    "elvisrgdc",
    "sameepdhakne_np",

]


def get_json(user_name):
    api = "https://www.instagram.com/{0}/?__a=1".format(user_name)
    try:
        r = requests.get(api)
    except requests.exceptions.ConnectionError:
        print("connection error")
        return
    if r.status_code != 200:
        return
    j = r.json()
    return j


# json_bhandari = get_json("bhandariayush_")
# if json_bhandari:
#     bhandari = InstaProfile(json_bhandari)
#
# print(bhandari.user_name, bhandari.followers)


def get_followers(json):
    value = json["graphql"]
    value1 = value["user"]
    value2 = value1["edge_followed_by"]
    value3 = value2["count"]
    return value3


dict = {}
list2 = []
for i in list_username:
    if get_json(i) is None:
        dict[i] = 0
    else:
        dict[i] = get_followers(get_json(i))
print(len(list_username),"without sorting")
list1 = sorted(dict.items(), key=lambda x: x[1], reverse=True)
for i in list1:
    list2.append(i[0])
print(len(list2), "after sorting")
print(list2)
