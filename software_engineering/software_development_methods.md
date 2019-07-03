# Software Development Methodologies(软件开发方法)

## Contents

### Software Process 软件流程
- A software process (also knows as software methodology) is **a set of related activities** that **leads to the production of the software**. These activities may involve the development of the software **from the scratch**, or, **modifying an existing system**.
- Any software process must include the following **four** activities (Each one includes sub-activities)
  - Software specification (or requirements engineering) 定义软件主要功能及其约束条件
  - Software design and implementation 设计软件以及实现
  - Software verification and validation 软件确认及验证
  - Software evolution (software maintenance) 根据客户需求以及市场变化修改软件
- Software process 是复杂的，依赖于所作的决定。不存在理想的process，大多数的组织都形成了自己的software process，critical system有非常结构化的process，而商业系统中，因为需求变化非常快，所以会更灵活且不那么正式的process会更高效一些。
- Plan-driven process VS Agile process
  - Plan-driven process is a process where all the activities are planned first and the progress is measured against the plan
  - Agile process, planning is incremental and it is easier to change the process to reflect requirement changes

### Software Development Methods
#### Waterfall (a.k.a. Traditional) 瀑布模型，又称传统模型
- ***Requirements***, ***Design***, ***Implementation***, ***Testing*** and ***Maintenance***
- Sequential approach(顺序方法)，process中的每一个activity都被表示为一个单独的phase，线性排列，在这个模型中，所有的activities都需要在开始实施之前计划好 (Plan-driven process)
- 原则上，在瀑布模型中，每一步都需要在上一步完成之后进行，然而在实际应用中，这些phases会有重叠部分，而且信息会相互交叉，因此这个software process并不是简单线性进行的，每一阶段产生的文件都可能会因为变化而进行改变
- 原则上讲，瀑布模型应当用于**所有需求都充分得到理解**并且确保**在开发过程中不会改变**的项目中
#### Prototyping
- A prototype is a version of a system or part of the system that’s developed **quickly to check the customer’s requirements** or **feasibility of some design decisions**.
- It is useful when a customer or developer is not sure of the requirements, or of algorithms, efficiency, business rules, response time, etc.
- A software prototype can be used in
  - **Requirements engineering**, a prototype can help with the elicitation and validation of system requirements
  - **System design**, a prototype can help to carry out deign experiments to check the feasibility of a proposed design
- The phases of a prototype
  - Establish objectives 在process一开始就应该清楚地知道objectives
  - Define prototype functionality 决定prototype的输入和期望输出，为了减少成本，可以忽略如响应时间以及内存利用等与objectives无关的功能（如果相关，则不可忽略）
  - Develop the prototype 最初的prototype只包含用户界面 
  - Evaluate the prototype 用户会使用prototype之后，他们会发现requirement errors，利用用户提供的反馈意见改善prototype
- Prototype不是一个单独完整的开发方法，但是是一个可以在增量、螺旋以及其他开发方法中利用到的一个方法
#### Incremental Development 增量开发

#### Spiral Model 旋螺模型

#### Iterative Development 迭代开发

#### Extreme Programming (XP) 极限编程
#### Feature Driven Development (FDD) 功能驱动开发
#### Joint Application Development (JAD) 联合应用开发 
#### Lean Development (LD) 精益软件开发
#### Rapid Application Development (RAD) 快速应用开发
#### Rational Unified Process (RUP) 统一软件开发过程
#### Systems Development Life Cycle (SDLC) 系统开发生命周期

#### Agile - *Scrum 
#### Agile - Crystal Methods 水晶模型
#### Agile - Dynamic Systems Development Model (DSDM) 动态系统开发模型
#### Agile - *Agile Software Development 敏捷软件开发 
- Agile methods refers to a group of software development models based on the **increamental** and **iterative** approach, in which the increments are small and typically, new releases of the system are created and made available to customers every few weeks.







## References
- Software Process and Software Process Models：https://medium.com/omarelgabrys-blog/software-engineering-software-process-and-software-process-models-part-2-4a9d06213fdc
