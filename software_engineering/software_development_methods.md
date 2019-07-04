# Software Development Methodologies(软件开发方法)

## Contents

### Software Engineering
#### Software Process 软件流程
- A software process (also knows as software methodology) is **a set of related activities** that **leads to the production of the software**. These activities may involve the development of the software **from the scratch**, or, **modifying an existing system**.
- Any software process must include the following **four** activities (Each one includes sub-activities)
  - Software specification (or requirements engineering) 定义软件主要功能及其约束条件
  - Software design and implementation 设计软件以及实现
  - Software verification and validation 软件确认及验证
  - Software evolution (software maintenance) 根据客户需求以及市场变化修改软件
- Software process 是复杂的，依赖于所作的决定。不存在理想的process，大多数的组织都形成了自己的software process，critical system有非常结构化的process，而商业系统中，因为需求变化非常快，所以会更灵活且不那么正式的process会更高效一些。
#### Reuse-oriented Software Engineering
- 它试图使用现有的与自己需求类似的设计或者代码（也可能经过测试的代码），对其进行修改，并将其合并到新系统中
- Phases
  - Component Analysis 根据给定的需求规范进行搜索相应的组件，一般没有完全匹配的，搜索到的组件一般只能提供所需的一部分功能
  - Requirement Modification 更具得到的组件分析需求，并根据需求修改这些组件，如果不能根据需求进行修改，那么就需要重新进行component analysis找相应的替代解决方案了
  - System Design with Reuse 设计系统框架或者重用某一已存在的系统框架，设计者应该将复用组件考虑进来并组织好相应的框架，如果一些组件没办法获取，那么就需要自己进行设计
  - Development and Integration 集成组建并创建新系统
- 一般会有三种软件组建是可以重用到reuse-oriented process的
  - Web services 根据well-know service standards进行开发的web service
  - Collection of objects e.g.像.NET或Java EE 通过一个框架组件里面集成的包
  - Standalone software systems that are configured for use in a particular environment.
- pros and cons
  - 减少需要开发的软件数量，并减少风险以及降低成本，而且可以更快交付软件产品
  - 需求会进行妥协，因此所开发的软件并不真正符合用户的需求
  - 对于系统的更新的控制会丢失，因为可重用组件的控制权不在用它们的组织手里

### Software Development Methods
#### Waterfall (a.k.a. Traditional) 瀑布模型，又称传统模型
- ***Requirements***, ***Design***, ***Implementation***, ***Testing*** and ***Maintenance***
- Sequential approach(顺序方法)，process中的每一个activity都被表示为一个单独的phase，线性排列，在这个模型中，所有的activities都需要在开始实施之前计划好 (Plan-driven process)
- 原则上，在瀑布模型中，每一步都需要在上一步完成之后进行，然而在实际应用中，这些phases会有重叠部分，而且信息会相互交叉，因此这个software process并不是简单线性进行的，每一阶段产生的文件都可能会因为变化而进行改变
- 原则上讲，瀑布模型应当用于**所有需求都充分得到理解**并且确保**在开发过程中不会改变**的项目中
- 不适合需要长时间开发的大项目或者需求模糊的项目，不能支持与客户频繁的见面
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
- 适合于需求不够清晰的时候，但需要好的展现工具，同时，训练团队进行prototype的成本可能会很高
#### Incremental Development 增量开发
- Incremental development是基于开发initial implementation的想法，将这个initial implementation展现给用户，并且使用用户的反馈意见进行版本改进直到完成可交付的系统的开发
- 每一个system increment都反映了用户的某一功能需求，一般来说，系统最开始的增量应该包括最重要或者最紧急的功能，因为这意味着客户可以在开发早期介入评估所开发的系统是否符合他们的需求，如果不符合，只需要改当前的increment或者接下来的功能或increment，不会是全盘进行修改
- 可以是plan-driven或者agile，也可以是两者皆有
  - plan-driven incremental：需要提前辨识系统增量
  - agile incremental：只需要辨识前期增量，后期增量则取决于进度和客户所认为地优先级
- 适合大项目，修改需求的成本较waterfall更低，小项目不适合
#### Spiral Model 螺旋模型
- Spiral model是risk-driven模型，在这个模型里，process并不是线性的一系列activities，而是螺旋式的
- 它包含了waterfall和prototyping的最优特点，以及引入了一个新的组成：risk-assessment
- 螺旋的每一圈都代表着一个phase，因此第一圈与系统可行性相关，第二圈关注需求定义，第三圈关注系统设计，每一圈都分为一下四部分
  - Objective setting 定义在这一个phase的目标和风险
  - Risk assessment and reduction 对于每一个被辨别出的项目风险进行详细分析，且采取行动降低风险。e.g.如果需求有风险是不合适的，那么就可能需要开发一个prototype了
  - Development and validation 在风险评估之后，系统的process model选定，所以如果风险如果是在用户界面这里，那么我们必须设计一个用户界面的prototype，如果存在风险的是这个开发的process，那么我们就需要转而使用waterfall
  - Planning 对项目进行审查，并决定是否继续进行下一步
- Spiral对帮助人们思考软件过程的迭代很有影响力，且引入了风险驱动的开发方法。但是实践里很少有用到这个模型。
- 适合高风险或者大项目，这些项目通常需求不清晰，风险可能是成本、时间、性能、用户界面等。但是风险分析需要高度专业化，项目的成败很大程度上取决于风险分析
#### Iterative Development 迭代开发
- Iterative development旨在通过构建**所有的components的所有功能**的一小部分来开发系统
- Phases of Iterative Development
  - Inception 目标是为系统构建商业用例。应该辨别所有将与系统交互的外部实体并定义这些交互行为，然后利用这个来评估这个系统对商业的意义，如果意义不大，这个project就可以取消了
  - Elaboration 我们了解问题领域以及架构框架，制定项目计划并识别风险
  - Construction 用通过对需求的分析、设计、实现和测试而产生的可用代码，逐步填充架构。这个系统的组件是相互依赖的，并且在此阶段，会并行进行开发这些组件并最后集成。在这一阶段过后，一个完成的软件就可供使用了。
  - Transition 将系统交付到生产操作环境中
- 所有的phases只会进行一次，而construction这个phase则会因为每一个系统的功能的完善在每次增量中被访问
- 适合大项目，修改需求的成本较waterfall更低，小项目不适合
#### Feature Driven Development (FDD) 功能驱动开发 Jeff De Luca and Peter Coad 
- Process 
  - Develop an overall model (10 percent initial, 4 percent ongoing)
  - Build a features list (4 percent initial, 1 percent ongoing)
  - Plan by feature (2 percent initial, 2 percent ongoing)
  - Design by feature
  - Build by feature (77 percent for design and build combined)
#### Joint Application Development (JAD) 联合应用开发 
- Two employees of IBM, Chuck Morris and Tony Crawford, developed the JAD methodology in the late 1970s and began teaching the approach in to the 1980s.
- JAD is a requirements-definition and user-interface design methodology in which end-users, executives, and developers attend intense off-site meetings to work out a system's details. 
- JAD focuses on the business problem rather than technical details.
#### Lean Development (LD) 精益软件开发
- Lean Development focuses on the creation of change-tolerant software. 
#### Rapid Application Development (RAD) 快速应用开发
- Put less emphasis on planning and more emphasis on an adaptive process. 
#### Rational Unified Process (RUP) 统一软件开发过程
- RUP represents an iterative approach 
- 特点
  - 用例驱动
  - 以架构为中心
  - 迭代与增量式开发
#### Systems Development Life Cycle (SDLC) 系统开发生命周期
- The systems development life cycle (SDLC) is a conceptual model used in project management that describes the stages involved in an information system development project, from an initial feasibility study through maintenance of the completed application.
#### Agile - *Agile Software Development 敏捷软件开发 
- Agile methods refers to a group of software development models based on the **increamental** and **iterative** approach, in which the increments are small and typically, new releases of the system are created and made available to customers every few weeks.
- 通过更多的非正式沟通以减少文档撰写，最适合于需求在开发过程中快速变化的应用
- 一般一次迭代是1-4周
- 适合小-中型项目，需求不断变化且客户每一阶段都参与，有了有限的计划就能开始做项目，省钱省时，对于大项目来说，很难套用， 因为大项目往往需要文档记录
#### Agile - *Scrum 
- Its goal is to dramatically improve productivity in teams previously paralyzed by heavier, process-laden methodologies.
#### Agile - Crystal Methods 水晶模型 by Alistair Cockburn
- His focus is on the people, interaction, community, skills, talents, and communications with the belief that these are what have the first-order effect on performance. Process, he says, is important, but secondary.
#### Agile - Agile Modeling(AM)
#### Extreme Programming (XP) 极限编程
- It used to be thought that Extreme Programming could only work in small teams of fewer than 12 persons. However, XP has been used successfully on teams of over a hundred developers.
- Core practices
  - Fine scale feedback
    - Test driven development, Planning game, Whole team, Pair programming
  - Continuous process rather than batch
    - Continuous Integration, Design Improvement, Small Releases
  - Shared understanding
    - Simple design, System metaphor, Collective code ownership, Coding standards or coding conventions
  - Programmer welfare
    - Sustainable pace (i.e. forty hour week)
#### Agile - Dynamic Systems Development Model (DSDM) 动态系统开发模型 developed in the U.K. in the mid-1990s
- It is the evolution of rapid application development (RAD) practices.
- Principles
  - Active user involvement
  - Empowered teams that the authority to can make decisions
  - A focus on frequent delivery of products
  - Using fitness for business purpose as the essential criterion for acceptance of deliverables
  - Iterative and incremental development to ensure convergence on an accurate business solution
  - Reversible changes during development
  - Requirements that is baselined at a high level
  - Integrated testing throughout the life cycle
  - Collaboration and cooperation between all stakeholders

### Comparisons for Models
- Plan-driven process VS Agile process
  - Plan-driven process is a process where all the activities are planned first and the progress is measured against the plan
  - Agile process, planning is incremental and it is easier to change the process to reflect requirement changes
- Incremental VS Waterfall Model
  - 对于大部分商业，电子商务以及个人系统而言，incremental software development比waterfall更好
  - 增量地进行开发软件，软件的开发成本更低且在开发过程中更容易进行更改
  - Incremental适应客户的需求进行修改软件的成本大大降低，所需要重新进行的分析以及撰写的文档比waterfall少很多
  - 在开发的过程中获得客户的反馈意见会比在开发全部完成、进行测试且发布后再获取意见更容易
  - 对于Incremental而言，即使并不是所有的功能都被囊括进去，但是更快速地交付有用的软件。用户可以更早地进行使用软件并从中获利，incremental比waterfall更能提供这种可能性
- Increment VS Iterative VS Agile
  - Incremental approach的每次increment都会包括某一个功能的整体
  - Iterative的每次increment都会包括软件的所有功能的一小部分
  - Agile则是结合incremental和Iterative方法，对系统内所需的所有功能，一次只构建一个功能的一部分，然后逐渐完善每个功能以及添加系统需要的剩余的功能
  


## References
- Software Process and Software Process Models：https://medium.com/omarelgabrys-blog/software-engineering-software-process-and-software-process-models-part-2-4a9d06213fdc
- Software Development Methodologies：http://www.itinfo.am/eng/software-development-methodologies/
