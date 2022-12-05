import time
import requests
from bs4 import BeautifulSoup
import json
import csv
import time
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0'}
# pip install BeautifulSoup4
# pip install requests 
# data = {}
# for i in range(0, 17):
#     url = f"https://courses.newschool.edu/?term%5B%5D=202210&campus%5B%5D=GV&page={i}&mode=json&_=1670198429800"
#     headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0'}
#     response = requests.get(url, headers=headers)  # send html request
#     # print(response.text)
#     json_data = json.loads(response.text)
#     soup = BeautifulSoup(json_data["data"]["attributes"], 'html.parser')  # parse data
#     # print(soup)
#     # soup = soup.find_all("div",  {"class":"crse_id"})  # gets specific header
#     crse_id = soup.select("div[class*=crse_id]")
#     titles = soup.select("div[class*=title]")
#     credit = soup.select("div[class*=credit]")
#     i = 0
#     for course in crse_id:
#         # print(course)
#         # print(titles[i])
#         # print(credit[i])
#         course_num = course.select("p")
#         course_num_str = str(course_num[0])
#         course_num_str = course_num_str.replace("<p>", "").replace("</p>", "")
#         course_credit = credit[i].select("p")
#         course_credit_str = str(course_credit[0])
#         course_credit_str = course_credit_str.replace("<p>", "").replace("</p>", "")
#         title = titles[i].select("p")
#         title_str = str(title[0])
#         title_str = title_str.replace("<p>", "").replace("</p>", "")
#         data[course_num_str] = {}
#         data[course_num_str]["credits"] = course_credit_str
#         data[course_num_str]["title"] = title_str
#         #     # entry["credits"] = course_credit_str
#         # print(f"{course_num_str} {course_credit_str} credits")
#         i += 1
    
#     with open("new_school_course_numbers_with_title_credit_fall2022_nyc.json", "w") as outfile:
#         outfile.write(json.dumps(data, indent = 4))


# results = []
# total = 0
# with open("new_school_course_numbers_with_title_credit_fall2022.json", "r") as in_file:
#     data = json.load(in_file)
#     for course_id in data:
#         print(course_id)
#         url = f"https://courses.newschool.edu/courses/{course_id}/13942/"
#         response = requests.get(url, headers=headers)  # send html request
#         print(response.text)
#         # json_data = json.loads(response.text)
#         soup = BeautifulSoup(response.text, 'html.parser')  # parse data
#         print(soup)
    # output = {}
    # count = 0
    # for course_id in data:
    #     print(course_id)
    #     url = f"https://courses.newschool.edu/?term%5B%5D=202210&page=1&crse_id={course_id}&mode=json&_=1669857183697"
    #     response = requests.get(url, headers=headers)  # send html request
    #     # print(response.text)
    #     json_data = json.loads(response.text)
    #     soup = BeautifulSoup(json_data["data"]["attributes"], 'html.parser')  # parse data
    #     try:
    #         instructor_elements = soup.find_all("div", class_="instructor")
    #         day_elements = soup.find_all("div", class_="days")
    #         time_elements = soup.find_all("div", class_="times")
    #         count = 0
    #         output[course_id] = []
    #         for day in day_elements:
    #             day_num = day.select("p")
    #             day_num_str = str(day_num[0]).replace("<p>", "").replace("</p>", "").replace("<em class=\"fa fa-calendar\"></em>", "")
    #             instructor = instructor_elements[count].select("p")
    #             instructor_str = str(instructor[0]).replace("<p>", "").replace("</p>", "").replace("<b>Faculty</b>: ", "")
    #             _time_num = time_elements[count].select("p")
    #             _time_num_str =  str(_time_num[0]).replace("<p>", "").replace("</p>", "")
    #             section = {}
    #             section["day"] = day_num_str
    #             section["time"] = _time_num_str
    #             section["Instructor"] = instructor_str
    #             output[course_id].append(section)
    #             count += 1

    #         with open("sections_with_instructor_fall2022.json", "w") as outfile:
    #             outfile.write(json.dumps(output, indent = 4))
    #     except BaseException as e:
    #         print(e)
    #     time.sleep(0.333)

with open("sections_with_instructor_fall2022.json", "r") as outfile:
    with open("new_school_course_numbers_with_title_credit_fall2022_nyc.json", "r") as titles:
        with open("people.csv", "r") as people_file:
            with open("fall_2022_contact_hours_for_ptf.csv", "a") as csv_out:
                data = json.load(outfile)
                titles_data = json.load(titles)
                reader = csv.DictReader(people_file)
                csvwriter = csv.writer(csv_out, lineterminator='\n')
                csvwriter.writerow(["INSTRUCTOR","TITLE","COURSE NUMBER", "MEETINGS PER WEEK", "START TIME", "END TIME","PTF"])
                ptf = []
                for row in reader:
                    ptf.append(row["name"])
                instructor = []    
                for course_num in data :
                    for section in data[course_num]:
                        title = ""
                        if course_num in titles_data:
                            title = titles_data[course_num]["title"]                    
                        day = section["day"]
                        day = day.split(",")
                        _time = section["time"]
                        _time = _time.split(" - ")
                        _start_time = ""
                        _end_time = ""
                        if len(_time) > 1:
                            _start_time = _time[0]
                            _end_time = _time[1]
                            _ptf = False
                        if "," in section["Instructor"]:
                            section["Instructor"] = section["Instructor"].replace("and ", "")
                            instructors = section["Instructor"].split(", ")
                            for inst in instructors:
                                if inst not in instructor:
                                    instructor.append(inst)
                                    print(len(instructor))
                                if inst in ptf:
                                    _ptf = True
                                else :
                                    _ptf = False
                                csvwriter.writerow([inst, title,course_num, len(day), _start_time, _end_time, _ptf])
                        elif "and" in section["Instructor"]:
                            instructors = section["Instructor"].split(" and ")
                            for inst in instructors:
                                if inst not in instructor:
                                    instructor.append(inst)
                                    print(len(instructor))
                                if inst in ptf:
                                    _ptf = True
                                else :
                                    _ptf = False
                                csvwriter.writerow([inst, title,course_num, len(day), _start_time, _end_time, _ptf])
                        else:
                            if section["Instructor"] in ptf:
                                _ptf = True
                            else :
                                _ptf = False
                            if section["Instructor"]  not in instructor:
                                instructor.append(section["Instructor"])
                                print(len(instructor))
                            print([section["Instructor"],title,course_num, len(day), _start_time, _end_time, _ptf])
                            csvwriter.writerow([section["Instructor"],title,course_num, len(day), _start_time, _end_time, _ptf])
                            

        

    # soup = soup.select("div[class*=crse_crn]")
    # count += len(soup)
    # entry = {}
    # entry["course_id"] = course_id
    # entry["count"] = len(soup)
    # results.append(entry)
    # with open("new_school_selction_numbers_winter.json", "w") as outfile:
    #     outfile.write(json.dumps(results, indent = 4))
    # print(count)

# with open("contact_hours_fall.json", "r") as contact_hours:
#     with open("fall_2022_contact_hours.csv", "a") as csv_out:
#         _data = json.load(contact_hours)
#         csvwriter = csv.writer(csv_out, lineterminator='\n')
#         csvwriter.writerow(["COURSE NUMBER", "DAYS PER WEEK", "START TIME", "END TIME"])

#         for course_num in _data :
#             for section in _data[course_num]:
#                 day = section["day"]
#                 day = day.split(",")
#                 _time = section["time"]
#                 _time = _time.split(" - ")
#                 if len(_time) > 1:
#                     _start_time = _time[0]
#                     _end_time = _time[1]
#                     csvwriter.writerow([course_num, len(day), _start_time, _end_time])

