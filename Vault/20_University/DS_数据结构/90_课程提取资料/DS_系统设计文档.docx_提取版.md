---
id: extract-ds-5d7326ce
type: extract
status: extracted
course: DS
source:
  - "[[91_Raw-Archive/DOC/DS_系统设计文档.docx_资料_未知日期_5d7326ce.docx]]"
source_pages: all
source_hash: "5d7326ceb9c545639682f200a4f62b143d3d077d4cf6be538c52794dac16ae60"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 系统设计文档.docx：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

系统设计文档

项    目：     教学管理系统设计    

学生姓名：          李尚凯         

学    号：       2024317220214     

专业班级：      计算机类2402班    

2025 年 6 月 10 日

目录

1.代码结构框架	3

1.1头文件	3

1.1.1 common.h	3

1.1.2 course.h	3

1.1.3 enrollment.h	4

1.1.4 global.h	5

1.1.5 learning_path.h	5

1.1.6 logger.h	6

1.1.7 login.h	7

1.1.8 prerequisite.h	7

1.1.9 student.h	8

1.1.10 teacher.h	9

1.2源文件	10

1.2.1 course.cpp	10

1.2.2 enrollment.cpp	12

1.2.3 global.cpp	12

1.2.4 learning_path.cpp	13

1.2.5 logger.cpp	14

1.2.6 login.cpp	14

1.2.7 main.cpp	15

1.2.8 prerequisite.cpp	16

1.2.9 student.cpp	17

1.2.10 teacher.cpp	19

1.3 数据文件	20

1.3.1 admin.txt	20

1.3.2 courses.txt	20

1.3.3 enrollments.txt	20

1.3.4 log.txt	20

1.3.5 prerequisites.txt	21

1.3.6 student.txt	21

1.3.7 students.txt	21

1.3.8 teacher.txt	21

1.3.9 teachers.txt	21

1.代码结构框架

1.1头文件

1.1.1 common.h

功能分析：

该头文件用于定义整个教学管理系统中会频繁使用的一些常量、宏定义、头文件引用以及公共函数声明。

具体内容：

1. 宏定义防止重复包含：

   #ifndef COMMON_H / #define COMMON_H / #endif

   防止头文件在多个源文件中被重复包含，导致重定义错误。

2. 宏定义 “_CRT_SECURE_NO_WARNINGS”：

   该宏用于在 Windows 平台下关闭对不安全函数（如 strcpy、scanf 等）的编译器警告提示，适用于 Visual Studio 开发环境。

3. 宏定义 “NAMESIZE”：

   定义名称最大长度为 100，用于统一限制如姓名、课程名等字符串长度。

4. 引入标准库头文件：

   - <iostream>：用于输入输出流操作。

   - <cstring>：用于字符串处理函数，如 strcpy、strlen 等。

5. 使用标准命名空间 `std`：

   避免每次使用 cout、cin 等都加上 std:: 前缀，简化代码书写。

6. 声明一个公共函数：

   void clearScreen();：声明了一个清屏函数，定义在 “main.cpp” 文件中实现。通常用于控制台程序中清空屏幕内容以增强交互体验。

用途总结：

common.h 是系统中的通用头文件，用于集中管理一些系统级宏定义、常用头文件和工具函数声明，提升代码复用性和可维护性。

1.1.2 course.h

功能分析：

该头文件定义了教育管理系统中“课程”的数据结构及其管理方式，采用二叉搜索树（BST）组织课程数据，便于高效查询、插入与遍历。

具体内容：

1. 宏定义与头文件引用：

   - 使用 “#ifndef COURSE_H / #define COURSE_H / #endif” 避免重复包含。

   - “#define _CRT_SECURE_NO_WARNINGS” 关闭不安全函数警告（针对 Visual Studio 环境）。

   - 引入 “common.h” 文件，继承其中的公共常量与函数。

2. 结构体 Course：

   定义课程对象的数据结构，包含：

   - “int id”：课程编号。

   - “char name[NAMESIZE]”：课程名称。

   - “int credits”：课程学分。

   - “Course* left, right”：指向左右子节点，用于构建二叉搜索树结构。

   - 构造函数 “Course(int _id, const char* _name, int _credits)”：用于初始化课程对象。

3. 类 CourseBST（课程二叉搜索树）：

   用于对课程进行插入、查找、遍历、存取文件等操作。

   - 成员变量：

     - “Course* root”：指向 BST 的根节点。

   - 私有成员函数：

     - “Course* insert(Course* node, int id, const char* name, int credits)”：递归插入课程。

     - “Course* find(Course* node, const char* name)”：递归查找课程。

     - “void inorder(Course* node)”：中序遍历课程（一般用于排序输出）。

   - 公有成员函数：

     - “CourseBST()”：构造函数，初始化根节点。

     - “void addCourse(int id, const char* name, int credits)”：插入新课程。

     - “Course* findCourse(const char* name)”：查找课程（封装接口）。

     - “void displayCourse()”：显示所有课程（调用中序遍历）。

     - “void saveToFile(const std::string& filename)”：将课程信息保存至文件。

     - “void loadFromFile(const std::string& filename)”：从文件加载课程信息。

   - 静态成员：

     - “DEFAULT_FILE”：默认课程文件路径为 “courses.txt”。

用途总结：

“course.h” 是课程管理模块的核心，定义了用于存储课程信息的结构体 “Course” 和用于管理课程的二叉搜索树类 “CourseBST”，提供课程的增、查、遍历、文件读写等核心功能，适用于整个教育管理系统中课程信息的统一管理与操作。

1.1.3 enrollment.h

功能分析：  

该头文件用于定义“选课管理”模块的结构和功能，实现学生选课与退课、查询选课信息、以及选课数据的文件持久化。

具体内容：

1. 宏定义与头文件引用：

   - 使用 “#ifndef ENROLLMENT_H / #define ENROLLMENT_H / #endif” 防止重复包含。

   - “#define _CRT_SECURE_NO_WARNINGS” 用于屏蔽不安全函数的编译器警告。

   - 引入头文件 “<iostream>” 和 “<cstdio>” 提供输入输出支持。

   - 使用命名空间 “std”。

2. 宏定义 “MAX_ENROLLMENTS”：

   - 设置选课记录的最大数量为 1000，限制 Enrollment 数组的大小。

3. 结构体 Enrollment：

   - 表示一条选课记录，包含：

     - “int studentId”：学生编号。

     - “int courseId”：课程编号。

   - 每一条记录表示某个学生选修了某门课程。

4. 类 EnrollmentList：

   实现对所有选课记录的管理。

   - 私有成员变量：

     - “Enrollment enrollments[MAX_ENROLLMENTS]”：用于存储选课记录的数组。

     - “int count”：当前记录的数量，用于控制添加位置和遍历上限。

   - 公有成员函数：

     - “EnrollmentList()”：构造函数，初始化选课列表。

     - “void enroll(int studentId, int courseId)”：添加选课记录。

     - “void unenroll(int studentId, int courseId)”：删除一条选课记录。

     - “void getCoursesByStudent(int studentId)”：根据学生编号列出他所选的所有课程。

     - “void getStudentsByCourse(int courseId)”：根据课程编号列出所有选修该课的学生。

     - “void saveToFile()”：将所有选课记录保存到文件中（默认文件名应在实现中定义）。

     - “void loadFromFile()”：从文件中加载所有选课记录。

用途总结：

“enrollment.h” 是教育管理系统中用于处理“选课信息”的核心头文件，定义了选课记录的存储结构和相关操作类 “EnrollmentList”，支持选课、退课、按学生或课程查询选课信息，以及将数据保存或加载到本地文件，实现基础的选课管理功能。

1.1.4 global.h

功能分析：  

该头文件用于声明全局变量，用于跨模块共享当前用户的身份信息，实现用户权限管理或用户身份识别等功能。

具体内容：

1. 宏定义与头文件引用：

   - 使用 “#ifndef GLOBAL_H / #define GLOBAL_H / #endif” 防止头文件重复包含。

   - “#define _CRT_SECURE_NO_WARNINGS” 用于关闭编译器关于不安全函数的警告（主要针对 Windows 平台的 Visual Studio）。

   - 引入 “<string>” 头文件，用于支持 “std::string” 类型。

2. 全局变量声明（使用 extern）：

   - “extern int currentUserId”：当前用户的 ID。使用 “extern” 说明该变量将在某个源文件中定义，这里仅作声明，允许其他模块共享。

   - “extern std::string currentUserRole”：当前用户的角色，例如 "student"、"teacher" 或 "admin"，用于控制系统中的操作权限和显示内容。

用途总结：

“global.h” 提供了跨文件访问当前登录用户身份信息的手段。通过声明全局变量 “currentUserId” 和 “currentUserRole”，系统的各个模块（如课程管理、选课系统等）都可以根据当前用户的身份进行权限控制和逻辑处理，是实现多用户角色控制的关键接口文件。

1.1.5 learning_path.h

功能分析：  

该头文件定义了“学习路径规划”模块的核心类 LearningPath，用于基于图论算法（如拓扑排序、最短路径等）计算课程的最优学习路径，支持课程先修关系的表示与路径规划。

具体内容：

1. 宏定义与头文件引用：

   - 使用 “#ifndef LEARNING_PATH_H / #define LEARNING_PATH_H / #endif” 防止头文件重复包含。

   - “#define _CRT_SECURE_NO_WARNINGS” 关闭不安全函数警告。

   - “#define MAX_COURSES 1000” 设置图中最多允许的课程节点数。

2. 类 LearningPath：

   表示一个有向图结构的课程网络，并实现最短路径求解等功能。

   - 私有成员变量：

     - “int graph[MAX_COURSES][MAX_COURSES]”：课程先修关系图的邻接矩阵表示。

     - “int inDegree[MAX_COURSES]”：每个节点的入度，用于拓扑排序。

     - “int distance[MAX_COURSES]”：用于记录最短路径的距离。

     - “int path[MAX_COURSES]”：用于记录路径上每个节点的前驱，便于回溯完整路径。

     - “int totalCourses”：课程总数，用于控制循环边界。

   - 公有成员函数：

     - “LearningPath()”：构造函数，初始化图结构。

     - “void addEdge(int from, int to)”：添加一条先修关系边，从课程 from 到课程 to，表示学习 to 必须先完成 from。

     - “void setTotalCourses(int total)”：设置课程总数量。

     - “void shortestPath(int start, int end)”：计算从课程 start 到课程 end 的最短路径，考虑先修关系。

     - “void loadFromFile(const char* filename)”：从文件中读取课程依赖关系并构建图结构。

用途总结：  

“learning_path.h” 是系统中用于学习路径优化规划的模块头文件，适用于具备课程先修依赖的教育体系。通过图结构存储课程之间的依赖关系，支持最短路径分析，有助于推荐学生合理的学习顺序，实现智能教学规划与路径优化。

1.1.6 logger.h

功能分析：  

该头文件用于定义系统操作日志记录功能，提供统一的操作记录接口 logOperation，用于跟踪和审计用户的关键行为。

具体内容：

1. 宏定义与头文件引用：

   - 使用 “#ifndef LOGGER_H / #define LOGGER_H / #endif” 防止头文件重复包含。

   - “#define _CRT_SECURE_NO_WARNINGS” 用于关闭关于不安全函数的编译警告。

   - 引入 “<string>” 头文件，支持字符串类型参数。

2. 函数声明：

   - “void logOperation(int userId, const std::string& userRole, const std::string& operation)”：

     - 用于记录一项用户操作。

     - 参数说明：

       - “int userId”：当前执行操作的用户编号。

       - “const std::string& userRole”：用户角色（如“student”、“teache“admin”等）。

       - “const std::string& operation”：用户执行的具体操作内容描述。

用途总结：  

“logger.h” 是系统日志功能的接口头文件，提供 logOperation 函数用于记录用户行为，适用于系统监控、安全审计、用户行为分析等场景。该接口可由多个模块统一调用，实现关键操作的追踪与日志管理。

1.1.7 login.h

功能分析：  

该头文件定义了用户登录模块的核心接口和相关结构体，用于实现用户身份验证与类型识别，支持学生、教师与管理员的登录处理。

具体内容：

1. 宏定义与头文件引用：

   - 使用 “#ifndef LOGIN_H / #define LOGIN_H / #endif” 防止头文件重复包含。

   - 引入 “<string>” 以支持字符串操作（尽管在当前头文件中未使用，但可为实现提供支持）。

2. 枚举类型 UserType：

   - 定义了用户类型，枚举成员包括：

     - “STUDENT”：学生用户。

     - “TEACHER”：教师用户。

     - “UNKNOWN”：未知用户（登录失败或身份不明）。

     - “ADMIN”：管理员用户。

3. 结构体 LoginResult：

   - 表示一次登录操作的结果，包含以下字段：

     - “bool success”：登录是否成功。

     - “UserType userType”：登录用户的类型。

     - “int id”：登录成功用户的编号。

4. 函数声明：

   - “LoginResult login()”：

     - 执行登录逻辑，并返回一个 LoginResult 结构体。

     - 用于界面或主函数调用，获取用户身份和权限信息。

用途总结：  

“login.h” 是系统用户认证模块的核心头文件，提供登录函数接口及结果结构，支持多用户类型的身份识别，适用于登录验证、权限控制等模块的上层调用，为整个教育管理系统的权限机制打下基础。

1.1.8 prerequisite.h

功能分析：  

该头文件定义了“课程先修关系”管理模块的核心类 PrerequisiteGraph，用于维护课程间的先修课依赖关系，支持查询和路径检测，实现课程依赖的管理与验证。

具体内容：

1. 宏定义与头文件引用：

   - 使用 “#ifndef PREREQUISITE_H / #define PREREQUISITE_H / #endif” 防止重复包含。

   - “#define _CRT_SECURE_NO_WARNINGS” 关闭编译器关于不安全函数的警告。

   - 引入 “<cstdio>” 用于文件操作。

2. 常量定义：

   - “MAX_COURSES = 1000”：课程最大数量，限制课程索引范围。

   - “MAX_PRE_REQ = 10”：每门课程最多支持 10 门先修课程。

3. 类 PrerequisiteGraph：

   表示课程先修关系的图结构，采用邻接表存储，支持深度优先搜索（DFS）实现依赖查询。

   - 私有成员变量：

     - “int prereqs[MAX_COURSES][MAX_PRE_REQ]”：邻接表，存储每门课程的先修课 ID 列表。

     - “int counts[MAX_COURSES]”：记录每门课程实际的先修课数量。

     - “bool visited[MAX_COURSES]”：访问标记，用于 DFS 遍历防止重复访问。

   - 私有成员函数：

     - “void dfs(int courseId)”：对某门课程执行深度优先遍历，通常用于遍历显示所有先修课程。

     - “bool dfsPath(int current, int target)”：检测从课程 current 是否存在路径到课程 target，判断先修关系链。

   - 公有成员函数：

     - “PrerequisiteGraph()”：构造函数，初始化数据结构。

     - “void addPrerequisite(int courseId, int prereqId)”：为某门课程添加一个先修课。

     - “void showAllPrerequisites(int courseId)”：显示指定课程的所有先修课程（直接和间接）。

     - “bool hasPrerequisitePath(int startId, int targetId)”：判断是否存在从 startId 到 targetId 的先修路径。

     - “void saveToFile()”：将先修关系数据保存至文件。

     - “void loadFromFile()”：从文件加载先修关系数据。

用途总结：  

“prerequisite.h” 是课程先修关系管理的重要模块，采用邻接表和 DFS 实现先修课的维护与查询。其功能有助于确保学习路径的合理性，避免课程学习顺序冲突，支持教学计划的智能化管理。

1.1.9 student.h

功能分析：  

该头文件定义了学生信息管理模块的核心结构体和类，实现学生信息的增删改查及基于哈希表的快速查找，并支持文件的持久化存储。

具体内容：

1. 宏定义与头文件引用：

   - 使用 “#ifndef STUDENT_H / #define STUDENT_H / #endif” 防止重复包含。

   - “#define _CRT_SECURE_NO_WARNINGS” 关闭编译器关于不安全函数的警告。

   - 引入标准库头文件 “<cstring>”、“<string>” 及自定义头文件 “common.h”。

   - 定义哈希表大小为 1000。

2. 类 Student：

   表示学生实体，包含基本属性及链表指针。

   - 成员变量：

     - “int id”：学生学号。

     - “char name[NAMESIZE]”：学生姓名，使用固定长度字符数组。

     - “int age”：学生年龄。

     - “int credits”：学生学分。

     - “Student* next”：指向链表中下一个学生节点，构成单向链表。

     - “Student* hashNext”：哈希冲突时链表的下一个指针，实现链式哈希。

   - 构造函数：

     - “Student(int _id, const char* _name, int _age, int _credits)”：初始化学生对象。

3. 类 StudentList：

   管理学生链表及哈希表，实现学生信息的快速查找与维护。

   - 私有成员变量：

     - “Student* head”：学生链表头指针。

     - “Student* hashTable[HASH_SIZE]”：基于哈希的索引数组，提升查找效率。

   - 私有成员函数：

     - “int hash(int id)”：计算学生 ID 的哈希值。

     - “void clear()”：清空所有学生信息，释放内存。

     - “void removeFromHashTable(int id)”：从哈希表中移除对应学生节点。

   - 公有成员函数：

     - 构造函数 “StudentList()” 和析构函数 “~StudentList()”。

     - “void Add_Student(int id, const char* name, int age, int credits)”：添加新学生。

     - “void deleteStudent(int id)”：删除指定 ID 的学生。

     - “void changeStudent(int id, const char* name, int age, int credits)”：修改学生信息。

     - “Student* findStudentByid(int id)”：根据 ID 查找学生。

     - “Student* findStudentByname(const char* name)”：根据姓名查找学生。

     - “void displayStudents()”：打印所有学生信息。

     - “void saveToFile(const std::string& filename = "students.txt")”：保存学生信息到文件。

     - “void loadFromFile(const std::string& filename = "students.txt")”：从文件加载学生信息。

用途总结：  

“student.h” 是教育管理系统中学生信息管理模块的核心文件，结合链表与哈希表实现高效的学生信息存储和查询，支持基本的增删改查操作，并通过文件持久化保证数据的保存与恢复，是学生管理的重要基础模块。

1.1.10 teacher.h

功能分析：  

该头文件定义了教师信息管理模块的结构体和类，实现教师信息的基本增删改查功能，采用链表结构存储教师数据，并支持文件持久化。

具体内容：

1. 宏定义与头文件引用：

   - 使用 “#ifndef TEACHER_H / #define TEACHER_H / #endif” 防止重复包含。

   - “#define _CRT_SECURE_NO_WARNINGS” 关闭编译器关于不安全函数的警告。

   - 引入 “<cstring>” 和自定义头文件 “common.h”，后者定义姓名最大长度 NAMESIZE。

2. 结构体 Teacher：

   表示教师实体，包含基本信息及链表指针。

   - 成员变量：

     - “int id”：教师编号。

     - “char name[NAMESIZE]”：教师姓名，固定长度字符数组。

     - “int age”：教师年龄。

     - “Teacher* next”：链表中指向下一教师节点的指针。

   - 构造函数：

     - “Teacher(int _id, const char* _name, int _age)”：初始化教师信息。

3. 类 TeacherList：

   采用单链表管理教师信息，提供基本的增删改查操作。

   - 私有成员变量：

     - “Teacher* head”：链表头指针。

   - 公有成员函数：

     - 构造函数 “TeacherList()” 和析构函数 “~TeacherList()”。

     - “void Add_Teacher(int id, const char* name, int age, bool doSave = true)”：添加教师，默认添加后保存数据。

     - “void deleteTeacher(int id)”：根据教师编号删除教师。

     - “void changeTeacher(int id, const char* name, int age)”：修改教师信息。

     - “Teacher* findTeacherByid(int id)”：通过编号查找教师。

     - “Teacher* findTeacherByname(const char* name)”：通过姓名查找教师。

     - “void displayTeachers()”：打印所有教师信息。

     - “void saveToFile(const std::string& filename)”：保存教师数据到文件。

     - “void loadFromFile(const std::string& filename)”：从文件加载教师数据。

     - “void clear()”：释放链表所有内存，重置头指针。

用途总结：  

“teacher.h” 是系统中教师管理模块的关键文件，采用链表结构方便动态管理教师信息，支持基本的增删改查及持久化操作，确保教师数据的完整与可持续维护，是教师信息管理的基础组件。

1.2源文件

1.2.1 course.cpp

1. 宏定义与头文件引用：

   - 引入头文件：

     - “#include "course.h"”：声明 Course 类与 CourseBST 类。

     - “#include "logger.h"”：用于记录日志操作。

     - “#include "global.h"”：包含全局变量，如 currentUserId、currentUserRole、DEFAULT_FILE 等。

     - “#include <cstring>”：用于字符串操作（strcpy、strcmp）。

2. 结构体 Course：

   表示课程实体，包含课程基本信息和用于构建二叉搜索树的左右子指针。

   - 成员变量：

     - “int id”：课程编号。

     - “char name[NAMESIZE]”：课程名称，定长字符数组。

     - “int credits”：课程学分。

     - “Course* left, *right”：左右子树指针，用于构建二叉搜索树。

 - 构造函数：

     - “Course(int _id, const char* _name, int _credits)”：根据传入参数初始化课程信息，并将左右指针设为 NULL。

3. 类 CourseBST：

   使用二叉搜索树（Binary Search Tree, BST）组织课程信息，支持高效的添加、查找、展示和持久化功能。

- 私有成员变量：

     - “Course* root”：二叉搜索树的根节点。

- 公有成员函数：

- 构造函数：

      - “CourseBST()”：初始化课程树，设置根节点为 NULL。

  - 基础操作：

       - “Course* insert(Course* node, int id, const char* name, int credits)”：

         递归插入课程节点，按课程名称进行字典序比较。

       - “Course* find(Course* node, const char* name)”：

         递归查找课程节点，按名称精确匹配。

       - “void inorder(Course* node)”：

         对课程树进行中序遍历，按课程名顺序输出所有课程信息。

   - 用户接口操作：

       - “void addCourse(int id, const char* name, int credits)”：

         外部接口，插入课程并自动保存数据，同时记录操作日志。

       - “Course* findCourse(const char* name)”：

         通过课程名称查找课程。

       - “void displayCourse()”：

         打印所有课程信息（编号、名称、学分）。

    - 文件操作相关：

       - “void saveToFile(const std::string& filename)”：

         保存当前课程树内容到指定文件，使用中序遍历确保有序性。

       - “void loadFromFile(const std::string& filename)”：

         从文件中逐行读取课程信息并插入树中，用于系统初始化时加载历史数据。

  - 辅助函数：

     - “void saveCourseToFile(FILE* fp, Course* node)”：

       将节点及其子树的课程信息写入文件，用于 saveToFile 函数。

用途总结：

“course.cpp” 是教育管理系统中课程管理模块的核心实现文件。它通过二叉搜索树结构组织课程信息，支持高效的课程插入、查找与显示，并实现对课程数据的文件保存与加载功能。同时通过日志模块记录用户对课程信息的操作，确保系统操作有迹可循，提升系统的数据完整性与可维护性。此模块是课程信息管理的基础支撑组件。

1.2.2 enrollment.cpp

1. 宏定义与头文件引用：

   - “#define _CRT_SECURE_NO_WARNINGS”：关闭 MSVC 编译器对不安全函数（如 fopen、scanf 等）的警告。

   - “#include "enrollment.h"”：包含选课模块的头文件，声明了 Enrollment 结构体与 EnrollmentList 类。

   - “#include <fstream>”：用于文件操作（虽然该文件主要使用了 C 风格 FILE*）。

   - “#include <cstring>”：用于字符串操作（但本文件中未使用 C 字符串函数，属于预留引用）。

2. 类 EnrollmentList：

   管理学生与课程之间的选课关系，使用数组保存 Enrollment 记录，支持选课、退课、查询和持久化。

   - 成员变量：

     - “Enrollment enrollments[MAX_ENROLLMENTS]”：固定大小的数组存储学生与课程的选课记录。

     - “int count”：当前选课记录数。

   - 构造函数：

     - “EnrollmentList()”：初始化时将 count 设为 0，并自动调用 loadFromFile() 从文件加载已有选课记录。

   - 公有成员函数：

     - “void enroll(int studentId, int courseId)”：

       学生选课操作。先检查是否重复选课，如果已选则不重复添加；若数组已满，提示上限；否则添加记录并保存到文件。

     - “void unenroll(int studentId, int courseId)”：

       学生退课操作。查找匹配记录并删除，同时将数组中后续元素向前移动，更新 count，最后保存到文件。

     - “void getCoursesByStudent(int studentId)”：

       查询某个学生所选的所有课程编号。若找不到记录，提示“该学生没有选修课程”。

1.2.3 global.cpp

1. 引用头文件：

   - “#include <string>”：引入 C++ 标准字符串库，支持使用 std::string 类型。

2. 全局变量定义：

   - “int currentUserId = 0”：

     定义当前登录用户的编号，初始为 0，通常表示未登录或默认用户。

   - “std::string currentUserRole = “δ֪””：

     当前用户角色，默认值为“δ֪”（意为“未知”），用于区分用户身份（如学生、教师或管理员）。

用途总结：

“global.cpp” 用于定义全局变量，以在整个教育管理系统中共享当前用户的身份信息。这些变量通常在用户登录时被赋值，并在操作日志记录或权限控制等模块中使用，是用户状态管理的基础组成部分。

1.2.4 learning_path.cpp

1. 引用头文件：

   - “#include "learning_path.h"”：包含 LearningPath 类的声明。

   - “#include <cstdio>”：提供 C 风格文件操作函数，如 fopen、fscanf、fclose。

   - “#include <climits>”：用于访问常量 INT_MAX。

   - “#include <cstring>”：用于内存初始化函数，如 memset。

   - “#include <iostream>”：使用标准输入输出（cout、endl）。

2. 类 LearningPath：

   该类用于构建课程之间的先修关系图，并通过广度优先搜索（BFS）计算某两门课程之间的最短路径。

   - 成员变量（定义在 learning_path.h）：

     - “int graph[MAX_COURSES][MAX_COURSES]”：邻接矩阵表示课程之间的先修关系。

     - “int inDegree[MAX_COURSES]”：每门课程的入度信息（暂未在路径算法中使用）。

     - “int distance[MAX_COURSES]”：记录从起始课程到每门课程的最短距离。

     - “int path[MAX_COURSES]”：记录最短路径中每个节点的前驱节点，便于路径回溯。

     - “int totalCourses”：课程总数，用于限制图的遍历范围。

   - 构造函数：

     - “LearningPath()”：初始化图、入度数组和路径信息，所有节点间距离设为 INT_MAX，path 数组设为 -1。

   - 公有成员函数：

     - “void setTotalCourses(int total)”：

       设置课程总数（图的有效节点数量）。

     - “void addEdge(int from, int to)”：

       添加有向边，表示“from”课程是“to”课程的先修课，同时增加“to”节点的入度。

     - “void loadFromFile(const char* filename)”：

       从指定文件读取先修课程对（每行两个整数），并建立图中的边关系。

       - 注意：调用 addEdge(b, a) 表示 b 是 a 的先修课。

     - “void shortestPath(int start, int end)”：

       计算从课程“start”到课程“end”的最短学习路径。

       - 采用广度优先搜索（BFS）计算最短路径。

       - 使用 distance[] 数组记录从起点到各节点的最短距离。

       - 使用 path[] 数组记录路径上的前一个课程编号。

       - 路径通过回溯 path[] 实现，并用栈输出正向路径。

       错误检测包括：

       - 输入编号越界；

       - 路径队列溢出（可能课程图过大或存在环）；

       - 回溯路径过长（可能存在依赖环或数据问题）；

       - 起点与终点间无路径存在时输出提示。

用途总结：

“learning_path.cpp” 是教育管理系统中学习路径推荐模块的核心实现文件。它通过构建课程之间的先修依赖图，支持基于广度优先搜索的最短路径分析，为学生规划合理的学习顺序提供决策支持。该模块可用于实现功能如“推荐下一门课程”、“查看课程依赖关系路径”等，是提升学习效率与系统智能化水平的重要组成部分。

1.2.5 logger.cpp

1. 引用头文件：

   - “#include "logger.h"”：包含 logOperation 函数的声明。

   - “#include <fstream>”：使用 std::ofstream 进行文件写入。

   - “#include <ctime>”：用于获取当前系统时间并格式化为时间戳。

2. 函数定义：

   - “void logOperation(int userId, const std::string& userRole, const std::string& operation)”：

     用于将系统中的用户操作记录到日志文件 log.txt 中，便于日后审计与跟踪。

   函数逻辑如下：

   - 使用 ofstream 以追加模式打开文件“log.txt”，若打开失败则直接返回；

   - 获取当前系统时间（time_t now），并使用 strftime 格式化为字符串时间戳（格式为“YYYY-MM-DD HH:MM:SS”）；

   - 将操作日志格式化写入日志文件，包括：

     - 当前时间

     - 用户ID

     - 用户角色（如学生、教师、管理员等）

     - 操作描述（如“添加课程：C++ 编程”）

   写入格式举例：

   [2025-06-10 14:32:08] 用户ID：101 角色：学生 操作：选修课程《高等数学》

   - 写入完毕后关闭文件流。

用途总结：

“logger.cpp” 是教育管理系统中的日志记录模块的实现文件，用于将用户操作写入日志文件。它提供了审计、安全分析和用户行为回溯的基础，特别适用于管理系统中需要留痕操作的功能。通过统一记录操作时间、用户身份和操作内容，该模块增强了系统的可维护性与透明性，是系统运行可追踪性的关键保障。

1.2.6 login.cpp

1. 引用头文件：

   - “#include "login.h"”：声明登录相关的结构和函数。

   - “#include "logger.h"”：用于记录登录操作日志。

   - “#include <iostream>”、“#include <fstream>”、“#include <sstream>”、“#include <string>”：支持输入输出、文件操作和字符串处理。

   - “#include "global.h"”：包含全局变量及用户状态信息。

2. 主要结构和枚举：

   - LoginResult 结构体：包含登录是否成功（bool success）、用户类型（UserType userType）、用户ID（int id）。

   - UserType 枚举：定义用户类型，如学生、教师、管理员和未知。

3. 函数定义：

   - LoginResult checkCredentials(int id, const string& password, const string& filename, UserType userType)：

     从指定的文件（学生、教师或管理员的账号文件）中验证用户ID和密码是否匹配。

     - 文件格式假设为“id password”每行一条记录。

     - 成功时返回登录成功结果，包括用户类型和ID。

     - 文件打开失败或匹配失败时返回失败结果。

   - LoginResult login()：

     登录流程入口。

     - 提示用户选择登录身份（学生、教师、管理员）。

     - 根据选择确定用户类型及对应的账号文件和角色名称。

     - 最多允许3次登录尝试。

     - 每次请求输入账号ID和密码，通过 checkCredentials 验证。

     - 登录成功时输出提示信息，记录登录成功日志，返回登录结果。

     - 登录失败时提示错误，记录失败日志，允许重试。

     - 3次失败后提示登录失败并退出程序。

4. 日志记录：

   - 成功或失败的登录均调用 logOperation 记录操作日志，包含用户ID、角色和操作描述，方便后续审计。

用途总结：

“login.cpp” 实现了教育管理系统的用户登录功能，支持多种身份（学生、教师、管理员）验证，确保用户身份安全。通过结合文件验证与日志记录，增强了系统的安全性和可追踪性。该模块是系统用户身份认证的关键入口，为后续权限控制和功能访问提供基础保障。

1.2.7 main.cpp

1. 引用头文件：

   - “#include "student.h"”：声明学生相关的数据结构和操作函数。

   - “#include "teacher.h"”：声明教师相关的数据结构和操作函数。

   - “#include "course.h"”：声明课程相关的二叉搜索树结构及操作。

   - “#include "enrollment.h"”：声明选课相关的数据结构及操作。

   - “#include "prerequisite.h"”：声明课程先修关系图及操作。

   - “#include "login.h"”：声明登录功能相关结构和函数。

   - “#include "learning_path.h"”：声明学习路径规划相关的数据结构和算法。

2. 主要数据结构实例化：

   - StudentList：管理所有学生信息。

   - TeacherList：管理所有教师信息。

   - CourseBST：管理课程的二叉搜索树。

   - EnrollmentList：管理学生选课情况。

   - PrerequisiteGraph：管理课程先修关系图。

   - LearningPath：管理并计算最优学习路径。

3. 函数定义：

   - void clearScreen()：

     清屏函数，根据操作系统调用不同命令实现界面清理。

   - void studentInterface(StudentList& studentList, CourseBST& courseBST, EnrollmentList& enrollmentList)：

     学生用户界面。

     - 提供查询学生信息、查询已选课程、选课、退课等功能。

     - 根据用户选择调用相应接口处理业务。

     - 操作完成后提示并清屏，允许连续操作直到退出。

   - void adminInterface(StudentList& studentList, CourseBST& courseBST, TeacherList& teacherList)：

     管理员用户界面。

     - 提供教师和学生的增删改查，课程添加，以及学生信息显示等功能。

     - 通过菜单选择实现对应管理操作。

     - 操作完成后提示并清屏，允许连续操作直到退出。

   - void teacherInterface(TeacherList& teacherList, CourseBST& courseBST, PrerequisiteGraph& preGraph, LearningPath& lp)：

     教师用户界面。

     - 提供课程信息查询、所有课程显示、添加先修关系、查询先修课程、先修关系判断及学习路径规划等功能。

     - 通过菜单选择调用对应函数实现。

     - 操作完成后提示并清屏，允许连续操作直到退出。

4. 主函数 main()：

   - 初始化所有核心数据结构（学生列表、教师列表、课程树、选课列表、先修图、学习路径）。

   - 从文件加载学生、教师、课程等数据。

   - 调用 login() 函数完成用户登录认证。

   - 根据登录结果的用户类型，进入对应的功能界面（学生、教师、管理员）。

   - 未知用户类型或登录失败时，输出提示并退出。

   - 程序结束前释放所有动态分配的内存，防止内存泄漏。

用途总结：

“main.cpp” 是教育管理系统的主入口，实现了基于用户身份的多角色界面切换和功能调用。通过整合学生、教师、课程、选课、先修关系及学习路径等模块，构建完整的系统业务流程。该文件负责系统初始化、用户登录、界面展示和用户操作流程控制，是系统运行的核心协调者。

1.2.8 prerequisite.cpp

1. 引用头文件：

   - “#include "prerequisite.h"”：声明课程先修关系图及相关操作。

   - “#include <cstdio>”：用于文件读写操作。

   - “#include <iostream>”：支持控制台输入输出。

2. 常量定义：

   - PREREQ_FILE：先修课程数据文件名，“prerequisites.txt”。

3. 类 PrerequisiteGraph 成员函数实现：

   - 构造函数 PrerequisiteGraph()：

     初始化每门课程的先修课计数为0，调用 loadFromFile() 加载文件中的先修关系。

   - void addPrerequisite(int courseId, int prereqId)：

     向指定课程添加先修课程。

     - 防止重复添加。

     - 检查先修课数量不超过最大限制。

     - 添加成功后调用 saveToFile() 保存数据。

     - 超出限制时输出警告。

   - void showAllPrerequisites(int courseId)：

     显示指定课程的所有先修课程编号。

     - 使用深度优先搜索（dfs）遍历先修课程。

     - 避免打印自身及重复课程。

   - void dfs(int courseId)：

     辅助深度优先搜索函数，用于递归打印所有先修课程。

   - bool hasPrerequisitePath(int startId, int targetId)：

     判断从起始课程到目标课程是否存在先修路径。

     - 使用辅助函数 dfsPath() 实现深度优先路径搜索。

   - bool dfsPath(int current, int target)：

     辅助递归函数，实现先修路径搜索。

     - 如果当前课程即目标课程返回真。

     - 遍历所有先修课程递归搜索路径。

   - void saveToFile()：

     将先修关系写入文件。

     - 以“课程ID 先修课ID”格式逐行保存。

   - void loadFromFile()：

     从文件读取先修关系。

     - 文件不存在时不报错，保持数据为空。

     - 读取格式为“课程ID 先修课ID”，并更新内部数据结构。

用途总结：

“prerequisite.cpp” 实现了课程先修关系图的管理，包括添加、查询和路径判断功能。通过文件持久化存储先修关系，支持系统重启后数据恢复。该模块是课程依赖管理的基础，确保课程学习顺序合理，有助于教学管理和学习路径规划。

1.2.9 student.cpp

1. 引用头文件：

   - “#include "student.h"”：声明学生类及学生链表相关结构和方法。

   - “#include "logger.h"”：用于记录学生操作日志。

   - “#include "global.h"”：包含当前用户信息等全局变量。

   - “#include <cstdio>”、“#include <cstring>”、“#include <iostream>”：支持文件操作、字符串处理及输入输出。

2. 主要类与结构：

   - Student 类：包含学生ID、姓名、年龄、学分等信息，以及指向链表和哈希表中下一个学生节点的指针。

   - StudentList 类：管理学生链表及哈希表，实现学生的增删改查和文件持久化。

3. 主要函数定义：

   - StudentList::Add_Student(int id, const char* name, int age, int credits)：

     新增学生记录。

     - 在链表尾部插入新学生。

     - 同时在哈希表中头插入，便于快速查找。

     - 保存学生数据到文件。

     - 记录添加操作日志。

   - StudentList::deleteStudent(int id)：

     根据学号删除学生。

     - 在链表中查找并删除对应节点。

     - 从哈希表中移除对应节点。

     - 保存数据并记录删除日志。

   - StudentList::changeStudent(int id, const char* name, int age, int credits)：

     修改学生信息。

     - 查找学生，更新姓名、年龄、学分。

     - 保存文件，记录修改前后信息的日志。

   - StudentList::findStudentByid(int id)：

     通过哈希表快速查找学生。

   - StudentList::findStudentByname(const char* name)：

     通过遍历链表查找学生。

   - StudentList::displayStudents()：

     遍历链表，打印所有学生信息。

   - StudentList::saveToFile(const string& filename)：

     将当前学生链表数据保存到文件。

     - 每行格式为“id name age credits”。

     - 操作完成后记录日志。

   - StudentList::loadFromFile(const string& filename)：

     从文件加载学生数据。

     - 读取文件内容，重建链表和哈希表。

     - 文件不存在时提示并以空列表开始。

     - 记录加载操作日志。

   - StudentList::hash(int id)：

     简单哈希函数，计算学号对哈希表大小的余数。

   - StudentList::clear()：

     清空链表及哈希表，释放内存。

   - StudentList::removeFromHashTable(int id)：

     辅助函数，从哈希表中移除指定学生节点。

4. 日志记录：

   - 每次添加、删除、修改、保存和加载操作均调用 logOperation 记录操作详情，便于系统审计和追踪。

用途总结：

“student.cpp” 实现了学生信息的管理模块，包括学生的增删改查和数据持久化，结合链表和哈希表提高操作效率。通过文件存储和日志记录保证数据安全和操作可追踪性，是学生管理系统的核心功能模块。

1.2.10 teacher.cpp

1. 引用头文件：

   - “#include "teacher.h"”：声明教师类及教师链表相关结构和方法。

   - “#include "global.h"”：包含全局变量及当前用户信息。

   - “#include "logger.h"”：用于记录教师操作日志。

   - “#include <cstdio>”、“#include <cstring>”、“#include <iostream>”：支持文件操作、字符串处理及输入输出。

2. 主要类与结构：

   - Teacher 类：包含教师工号、姓名、年龄，以及链表中下一个教师节点指针。

   - TeacherList 类：管理教师链表，实现教师的增删改查和文件持久化。

3. 主要函数定义：

   - TeacherList::Add_Teacher(int id, const char* name, int age, bool doSave)：

     添加教师记录。

     - 将新教师添加到链表尾部。

     - 如果 doSave 为真，则保存文件并记录添加日志。

   - TeacherList::deleteTeacher(int id)：

     根据工号删除教师。

     - 在链表中查找并删除对应节点。

     - 保存文件，记录删除操作日志。

   - TeacherList::changeTeacher(int id, const char* name, int age)：

     修改教师信息。

     - 查找教师，更新姓名和年龄。

     - 保存文件，记录修改操作日志。

   - TeacherList::findTeacherByid(int id)：

     通过工号查找教师。

   - TeacherList::findTeacherByname(const char* name)：

     通过遍历链表按姓名查找教师。

   - TeacherList::displayTeachers()：

     遍历链表，打印所有教师信息。

   - TeacherList::saveToFile(const string& filename)：

     将教师链表数据保存到文件。

     - 每行格式为“id name age”。

     - 操作完成后提示并记录日志。

   - TeacherList::loadFromFile(const string& filename)：

     从文件加载教师数据。

     - 文件不存在时提示并以空列表开始。

     - 读取文件内容，重建链表。

     - 加载时不保存文件，不触发保存日志。

   - TeacherList::clear()：

     清空链表，释放内存。

4. 日志记录：

   - 添加、删除、修改教师均记录操作日志，方便系统审计与追踪。

用途总结：

“teacher.cpp” 实现了教师信息管理模块，支持教师的增删改查及数据持久化。通过链表结构管理数据，结合日志记录和文件保存，保障数据安全和操作透明，是教师管理系统的关键组成部分。

1.3 数据文件

1.3.1 admin.txt

该文件用于存储管理者账号及密码信息，支持以下操作：

1.增加管理者账号：可新增管理者账户及对应密码信息

2.删除管理者账号：可移除指定管理者的账户记录

3.查询管理者账号：可通过关键词检索特定管理者的账户信息

4.修改管理者账号：可对现有管理者的账户信息（包括账号和密码）进行编辑更新

1.3.2 courses.txt

该文件用于存储学生选课科目及对应学科学分信息。可根据实际需求，对相关内容进行以下操作：

1.新增选课记录：录入学生所选科目及对应的学科学分；

2.删除选课记录：移除学生不再修读的科目及学分信息；

3.查询选课信息：通过学生姓名、学号或科目名称等关键词，检索对应学生的选课科目及学分；

4.修改选课信息：更正或调整已录入的科目名称、学分数值等内容。

1.3.3 enrollments.txt

该文件用于存储学生学号及其对应的选课编号信息。可根据需求，对相关数据进行以下操作：

1.新增数据记录：录入学生学号及所对应的选课编号；

2.删除数据记录：移除不再需要的学生学号与选课编号关联信息；

3.查询数据信息：通过学生学号或选课编号等关键词，检索对应的关联记录；

4.修改数据信息：更正或调整已录入的学号或选课编号内容

1.3.4 log.txt

该文件用于存储登录系统的人员信息及其具体操作记录。可针对相关内容执行以下操作：

1.新增记录：录入登录人员的身份信息（如用户名、账号等）及对应的操作详情（如操作时间、功能模块、操作内容等）；

2.删除记录：移除不再需要的人员信息或历史操作记录；

查询记录：通过人员姓名、账号、操作时间、操作类型等关键词，检索特定人员的登录信息及操作详情；

3.修改记录：更正或补充已录入的人员信息（如账号状态）或操作记录（如误记的操作内容）。

1.3.5 prerequisites.txt

文件用于存储课程的先修课程信息。可根据教学管理需求，对相关内容进行以下操作：

1.新增先修关系：录入课程与其先修课程的对应关联（如课程 A 的先修课程为课程 B）；

2.删除先修关系：移除不再适用的课程先修关联记录；

3.查询先修信息：通过课程名称或课程代码，检索该课程的先修课程列表及相关要求；

4.修改先修信息：调整或更正已录入的先修课程名称、代码或关联关系。

1.3.6 student.txt

该文件用于存储学生登录账号及密码信息。

1.3.7 students.txt

该文件用于存储学生登录人员的学号、姓名、年龄及学分总数信息。可根据管理需求，对相关数据进行以下操作：

1.新增数据：录入学生的学号、姓名、年龄及学分总数；

2.删除数据：移除不再需要的学生信息记录；

3.查询数据：通过学号或姓名等关键词，检索对应学生的年龄、学分总数等详情；

4.修改数据：更正或更新已录入的年龄、学分总数等信息。

1.3.8 teacher.txt

该文件用于存储学生登录账号及密码信息。

1.3.9 teachers.txt

该文件用于存储教师登录系统人员的基础信息，具体包括：

1.信息录入：可新增教师姓名、年龄等字段内容；

2.记录更新：支持修改已录入的年龄信息（姓名作为唯一标识原则上不允许修改）；

3.数据查询：可通过姓名检索对应教师的年龄信息；

4.记录维护：定期清理无效或过期的教师信息记录。 

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_数据结构_课程MOC|数据结构 MOC]]
