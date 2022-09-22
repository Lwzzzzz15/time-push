from courseBase import courseBase

courseList_Mon = [
    courseBase("马克思", "华二阶梯", 2, 10, 1, "10:30 - 12:10"),
    courseBase("企业价值评估", "华一604", 2, 11, 1, "14:00 - 17:30")
]

courseList_Tues = [
    courseBase("英语视听说", "华一315", 2, 19, 2, "8:30 - 10:10"),
    courseBase("无形资产评估", "华办605", 2, 11, 2, "18:30 - 21:30")
]

courseList_Wed = [
    courseBase("企业战略管理", "华办703", 2, 14, 3, "18:00 - 21:00")
]

courseList_Thur = [
    courseBase("中特社会主义理论与实践", "华二阶梯", 2, 18, 4, "10:30 - 12:10"),
    courseBase("中国税制专题", "华一202", 2, 16, 4, "14:00 - 17:30")
]

courseList_Fri = [
    courseBase("资产评估", "华一604", 9, 18, 5, "8:30 - 12:10"),
    courseBase("税收理论与政策", "华一202", 3, 13, 5, "14:00 - 17:30")
]

courseList_Sat = [
    courseBase("房地产金融", "华二阶梯", 2, 10, 6, "8:30 - 12:10"),
    courseBase("经济学分析", "华二阶梯", 10, 18, 6, "14:00 - 17:30")
]

courseList_Sun = [
    courseBase("学术规范与论文撰写", "华二阶梯", 12, 16, 7, "8:30 - 12:10")
]


semester_1_courseDict = {
    1: courseList_Mon,
    2: courseList_Tues,
    3: courseList_Wed,
    4: courseList_Thur,
    5: courseList_Fri,
    6: courseList_Sat,
    7: courseList_Sun
}
