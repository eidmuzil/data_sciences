#!/usr/bin/env python
# coding: utf-8

# # Seaborn :
# مكتبة من مكتبات البايثون لتصور البيانات على أساس مكتبة matplotlib  
#            توفر رسومات احصائية غنية بالمعلومات  
#            
#            - تساعدك على فهم وكتشاف  البيانات 
#            - تعمل وظائف التخطيط بها على اطر البيانات و المصفوفات 
#            - رسم الخرائظ الدلالية و الاحصائية 
#            - تتيح واجهة للمستخدم 
#            

# In[8]:


# مثال لمكتبة seaborn 
import seaborn as sns  

# تحميل ثيمات مختلفة 
sns.set_theme()
# تحميل البيانات 
tips = sns.load_dataset("tips")

# انشاء تصور 

sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
) 


# In[6]:


# تحميل البيانات 
dots = sns.load_dataset("dots")

sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate", col="align",
    hue="choice", size="coherence", style="choice",
    facet_kws=dict(sharex=False),
)


# # التقدير الإحصائي وأشرطة الخطأ
في كثير من الأحيان ، نحن مهتمون بمتوسط قيمة متغير واحد كدالة لمتغيرات أخرى. ستقوم العديد من وظائف المكتبة الاحصائية seaborn تلقائيًا بإجراء التقدير الإحصائي الضروري للإجابة على هذه الأسئلة:
# In[9]:


cond = sns.load_dataset("fmri") # loading the database 
sns.relplot(
    data=cond, kind="line",
    x="timepoint", y="signal", col="region",
    hue="event", style="event",
) # using line as kind of or graphic


# عندما يتم تقدير القيم الإحصائية ، سيستخدم seaborn bootstrapping لحساب فترات الثقة ورسم أشرطة الخطأ التي تمثل عدم اليقين في التقدير.
# 
# التقدير الإحصائي في seaborn يتجاوز الإحصاء الوصفي. على سبيل المثال ، من الممكن تحسين مخطط التشتت من خلال تضمين نموذج الانحدار الخطي (وعدم اليقين فيه) باستخدام lmplot ()

# In[12]:


sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")


# # التصور عن طريق display ()
# 
# تتطلب التحليلات الإحصائية معرفة حول توزيع
# المتغيرات في مجموعة البيانات الخاصة بك. تدعم وظيفة  عدة طرق لتصور 
# التوزيعات. وتشمل هذه التقنيات الكلاسيكية مثل الرسوم البيانية
# والأساليب الحسابية المكثفة مثل تقدير كثافة النواة

# In[14]:


sns.displot(data=tips, x="total_bill", col="time", kde=True)


# In[15]:


# حساب ورسم دالة التوزيع التراكمي التجريبي للبيانات

sns.displot(data=tips, kind="ecdf", x="total_bill", col="time", hue="smoker", rug=True)

 # catplolt () 
    تقدم هذه الدالة  مستويات مختلفة من التفاصيل. في أفضل مستوى
    ، قد ترغب في رؤية كل ملاحظة من خلال رسم مخطط "سرب"
     مخطط مبعثر يضبط مواضع النقاط على طول المحور الفئوي بحيث لا تتداخل
# In[16]:


# مثال 
sns.catplot(data=tips, kind="swarm", x="day", y="total_bill", hue="smoker")


# In[17]:


sns.catplot(data=tips, kind="violin", x="day", y="total_bill", hue="smoker", split=True)
#يمكنك استخدام تقدير كثافة لتمثيل التوزيع الأساسي الذي يتم أخذ عينات من النقاط منه

# jointplot() 
لعمل ملخص سريع و عملي لمجموعة البيانات 
لعمل مخطط مشترك يركز على علاقة واحدة 
رسم توزيع مشترك بين متغيرين مع التوزيعات الهامشية 
شكل الرسم التوضيحي احترافي و جميل 

# In[18]:


# مثال 
penguins = sns.load_dataset("penguins") # تحميل البيانات 
sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")

pairplot() 
يظهر التوزيعات المشتركة و الهامشية لجميع العلاقات ولكل متغير بنظره أوسع 

# In[19]:


# مثال لبيانات المثال السابق 
sns.pairplot(data=penguins, hue="species")


# ### لعمل رسومات معقدة 
PairGrid()
تعمل هذه الإداة من خلال الجمع بين وظائف التخطيط 
يمكنك استخدامها لانشاء رسومات معقدة بسطور من البرمجة 
تعد واجهة من واجهات برمجة التطبيقات العامة 
# In[20]:


# مثال 
g = sns.PairGrid(penguins, hue="species", corner=True)
g.map_lower(sns.kdeplot, hue=None, levels=5, color=".2")
g.map_lower(sns.scatterplot, marker="+")
g.map_diag(sns.histplot, element="step", linewidth=0, kde=True)
g.add_legend(frameon=True)
g.legend.set_bbox_to_anchor((.61, .6))

الافتراضات المعلنة والتخصيص المرن
تُنشئ Seaborn رسومات كاملة باستدعاء وظيفة واحدة: عندما يكون ذلك ممكنًا ، ستضيف وظائفها تلقائيًا تسميات محاور إعلامية ومفاتيح تشرح التعيينات الدلالية في الرسم البياني.

في كثير من الحالات ، سيختار seaborn أيضًا القيم الافتراضية لمعلماته بناءً على خصائص البيانات. على سبيل المثال ، استخدمت تعيينات الألوان التي رأيناها حتى الآن درجات ألوان مميزة (أزرق وبرتقالي وأحيانًا أخضر) لتمثيل مستويات مختلفة من المتغيرات الفئوية المعينة إلى تدرج اللون. عند تعيين متغير رقمي ، ستتحول بعض الوظائف إلى تدرج مستمر:
# In[21]:




sns.relplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="body_mass_g"
)

عندما تكون مستعدًا لمشاركة عملك أو نشره ، فربما تريد تحسين الشكل بما يتجاوز ما تحققه الإعدادات الافتراضية. يسمح Seaborn لعدة مستويات من التخصيص. يحدد العديد من السمات المضمنة التي تنطبق على جميع الأشكال ، ووظائفها لها معلمات موحدة يمكنها تعديل التعيينات الدلالية لكل قطعة ، ويتم تمرير وسيطات الكلمات الرئيسية الإضافية إلى مجموعات matplotlib الأساسية ، مما يسمح بمزيد من التحكم. بمجرد إنشاء رسم تخطيطي  ، يمكن تعديل خصائصها من خلال كل من واجهة برمجة التطبيقات seaborn وعن طريق التراجع إلى طبقة matplotlib لإجراء تعديلات دقيقة على الحبيبات:
# In[25]:


sns.set_theme(style="ticks", font_scale=1.25)
g = sns.relplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="body_mass_g",
    palette="crest", marker="x", s=100,
)
g.set_axis_labels("Bill length (mm)", "Bill depth (mm)", labelpad=10)
g.legend.set_title("Body mass (g)")
g.fig.set_size_inches(6.5, 4.5)
g.ax.margins(.15)
g.despine(trim=True)


# In[24]:


sns.set_theme(style="ticks", font_scale=1.25)
g = sns.relplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="body_mass_g",
    palette="rocket", marker="x", s=100,
)
g.set_axis_labels("Bill length (mm)", "Bill depth (mm)", labelpad=10)
g.legend.set_title("Body mass (g)")
g.fig.set_size_inches(6.5, 4.5)
g.ax.margins(.15)
g.despine(trim=True)


# In[ ]:





# In[ ]:




