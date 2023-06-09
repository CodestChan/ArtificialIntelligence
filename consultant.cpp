#define MAXINT 32767
#define MAXNUM 100
#define MAXSIZE 100
#include<fstream>
#include<iostream>
#include<string>
#include<stdlib.h>
using namespace std;
typedef struct
{
	int* base;
	int* top;
	int stacksize;
}Sps;
void InitStack(Sps& s)
{
	s.base = new int[MAXSIZE];
	if (!s.base) exit(OVERFLOW);
	s.top = s.base; 
	s.stacksize = MAXSIZE;
}
void push(Sps& s, int e)
{
	if (s.top - s.base == s.stacksize) cout << "stack is full already";
	*s.top = e;
	s.top++;
}
int pop(Sps& s, int& e)
{
	if (s.top == s.base) cout << "stack is empty already";
	--s.top;
	e = *s.top;
	return e;
}
typedef int Distance;
typedef struct
{
	string name;
	char code;
	string intrd;
}Scenery;
typedef struct
{
	Scenery vexs[MAXNUM];
	Distance arcs[MAXNUM][MAXNUM];
	int vexnum, arcnum;
}Sgraph;
void Putindata(Sgraph& G)
{
	G.vexnum = 10; G.arcnum=14;
	G.vexs[0].name = "大门"; G.vexs[0].code = '0'; G.vexs[0].intrd = "江西理工的大门，十分宽敞";
	G.vexs[1].name = "宿舍"; G.vexs[1].code = '1'; G.vexs[1].intrd = "学生生活居住的地方，共有17栋之多";
	G.vexs[2].name = "食堂"; G.vexs[2].code = '2'; G.vexs[2].intrd = "学生老师用餐场所，共有三层楼，每一层都有不同店面提供不同的餐饮";
	G.vexs[3].name = "信息学院"; G.vexs[3].code = '3'; G.vexs[3].intrd = "有关计算机专业的学生上课，实验的场所";
	G.vexs[4].name = "图书馆"; G.vexs[4].code = '4'; G.vexs[4].intrd = "拥有海量藏书，学生可以在此地自习";
	G.vexs[5].name = "阅道楼"; G.vexs[5].code = '5'; G.vexs[5].intrd = "学生上课，老师教学的教学楼之一";
	G.vexs[6].name = "文山楼"; G.vexs[6].code = '6'; G.vexs[6].intrd = "学生上课，老师教学的教学楼之一";
	G.vexs[7].name = "体育馆"; G.vexs[7].code = '7'; G.vexs[7].intrd = "学生进行众多活动及锻炼的场所";
	G.vexs[8].name = "操场"; G.vexs[8].code = '8'; G.vexs[8].intrd = "学生进行众多活动及体育课进行的主要场所";
	G.vexs[9].name = "八角塘"; G.vexs[9].code = '9'; G.vexs[9].intrd = "校园特色景点，是江西理工标志性景物";
}
void Createtu(Sgraph& G)
{
	for (int i = 0; i < G.vexnum; i++)
		for (int j = 0; j < G.vexnum; j++)
			G.arcs[i][j] = MAXINT;
	G.arcs[0][1] = 30; G.arcs[0][2] = 15; G.arcs[1][2] = 40; G.arcs[1][3] = 45;
	G.arcs[3][9] = 35; G.arcs[4][9] = 22; G.arcs[2][4] = 28; G.arcs[4][5] = 15;
	G.arcs[4][6] = 15; G.arcs[5][6] = 20; G.arcs[2][8] = 25; G.arcs[7][8] = 18;
	G.arcs[5][7] = 10; G.arcs[3][4] = 12;
	for (int a = 0; a < G.vexnum; a++)
	{
		for (int b = 0; b < G.vexnum; b++)
		{
			if (G.arcs[a][b] != MAXINT)G.arcs[b][a] = G.arcs[a][b];
		}
	}
}
void P1()
{
	cout << "******************************" << endl;
	cout << endl;
	cout << "    " << "欢迎来到校园咨询导航系统！" << endl;
	cout << "******************************" << endl;
	cout << endl;
}
void P2()
{
	cout << "   " << "请输入要查询的服务编号" << endl;
	cout << endl;
	cout << "   " << "扣1查询相关景点的信息" << endl;
	cout << "   " << "扣2查询景点间的最短路径" << endl;
}
void P3()
{
	cout << "  " << "0:大门"<<endl;
	cout << "  " << "1:宿舍"<<endl;
	cout << "  " << "2:食堂"<<endl;
	cout << "  " << "3:信息学院"<<endl;
	cout << "  " << "4:图书馆" << endl;;
	cout << "  " << "5:阅道楼" << endl;
	cout << "  " << "6:文山楼" << endl;
	cout << "  " << "7:体育馆" << endl;
	cout << "  " << "8:操场" << endl;
	cout << "  " << "9:八角塘" << endl;
}
void serve(Sgraph& s, char n)
{
	for (int i = 0; i < s.vexnum; i++)
	{
		if (s.vexs[i].code == n)cout << s.vexs[i].name << "：" << s.vexs[i].intrd;
	}
	cout << endl;
}
void P4()
{
	cout << endl;
	cout << "******************************" << endl;
	cout << endl;
}
void Short(Sgraph& G, int v0, int v9)
{
	Sps S; InitStack(S); int e, el[10]; int f = 0;
	int n = G.vexnum; int min; int v; int f1 = 1;
	bool s[10]; int path[10]; int D[10];
	for (v = 0; v < n; v++)
	{
		s[v] = false;
		D[v] = G.arcs[v0][v];
		if (D[v] < MAXINT) path[v] = v0;
		else path[v] = -1;
	}
	s[v0] = true; D[v0] = 0;
	for (int i = 0; i < n; i++)
	{
		min = MAXINT;
		for (int w = 0; w < n; w++)
		{
			if (!s[w] && D[w] < min)
			{
				v = w; min = D[w];
			}
		}
		s[v] = true;
		for (int w = 0; w < n; w++)
		{
			if (!s[w] && (D[v] + G.arcs[v][w] < D[w]))
			{
				D[w] = D[v] + G.arcs[v][w];
				path[w] = v;
			}
		}
	}
	push(S, v9); e = v9;     //变量e用来求出顶点的前置
	while (f1)               //f1用来循环条件判断
	{
		if (path[e] != v0)
		{
			e = path[e];
			push(S, e);
		}
		else f1=0;
	}
	push(S, v0);
	while (S.top != S.base)
	{
		el[f] = pop(S,e);     //el数组用来存储栈S弹出的值
		f++;
	}
	cout << "  " << "为您规划最短路线:";
	for(int i=0;i<f;i++)
	{
	   cout<<G.vexs[el[i]].name<<" ";
	} 
	cout << endl;
	cout << endl;
	cout << G.vexs[v0].name << "到" << G.vexs[v9].name << "的最短路径为：" << D[v9];
}
void Print(Sgraph& G)
{
	for (int i = 0; i < G.vexnum; i++)
	{
		for (int j = 0; j < G.vexnum; j++)
		{
			cout << G.arcs[i][j] << " ";
		}
		cout << endl;
		cout << endl;
	}
}
int main()
{
	Sgraph s; int t = 1; int select,s4,s5; int t2 = 1;
	Putindata(s); char s2, s3, s6;
	Createtu(s);
	P1();
	while (t)
	{
		while (t)
		{
			P2();
			P4();
			cin >> select;
			if (select == 1 || select == 2)
			{
				if (select == 1)
				{
					while (t2)
					{
						while (t2)
						{
							cout << "   " << "请输入要查询的景点编号：" << endl;
							cout << endl;
							P3();
							P4();
							cin >> s2;
							if (s2 < '0' || s2>'9')
							{
								P4();
								cout << "   " << "请输入正确的编号！" << endl;
								P4();
								break;
							}
							P4();
							serve(s, s2);
							P4();
							cout << "   " << "是否继续查询其他景点？" << endl;
							cout << "   " << "Yes：Y" << "  " << "No：N" << endl;
							P4();
							cin >> s3;
							if (s3 == 'Y')t2 = 1;
							else if (s3 == 'N') t2 = 0;
							else
							{
								P4();
								cout << "  " << "出错了，退出景点查询" << endl;
								t2 = 0;
								P4();
								break;
							}
						}
					}
				}
				if (select == 2)
				{
					while (t2)
					{
						while (t2)
						{
							cout << "   " << "请输入想要查询的两地的编号：" << endl;
							cout << endl;
							P3();
							P4();
							cin >> s4 >> s5;
							if ((s4 < 0 || s4>9) || (s5 < 0 || s5>9))
							{
								P4();
								cout << "   " << "请输入正确的编号！" << endl;
								P4();
								break;
							}
							P4();
							Short(s, s4, s5);
							P4();
							cout << "   " << "是否继续查询？" << endl;
							cout << "   " << "Yes：Y" << "  " << "No：N" << endl;
							P4();
							cin >> s3;
							if (s3 == 'Y')t2 = 1;
							else if (s3 == 'N') t2 = 0;
							else
							{
								P4();
								cout << "  " << "出错了，退出路径查询" << endl;
								t2 = 0;
								P4();
								break;
							}
						}
					}
				}
			}
			else
			{
				P4();
				cout << "   " << "请输入正确的序号！" << endl;
				P4();
				break;
			}
			P4();
			cout << "   " << "是否退出咨询系统？" << endl;
			cout << "   " << "Yes：Y" << "  " << "No：N" << endl;
			P4();
			cin >> s6;
			if (s6 == 'Y')t = 0;
			if (s6 == 'N')t = 1;
			t2 = 1;
		}
	}
	P4();
	cout << "    " << "感谢您的使用!再见" << endl;
} 
