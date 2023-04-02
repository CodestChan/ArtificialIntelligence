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
	G.vexs[0].name = "����"; G.vexs[0].code = '0'; G.vexs[0].intrd = "�������Ĵ��ţ�ʮ�ֿ�";
	G.vexs[1].name = "����"; G.vexs[1].code = '1'; G.vexs[1].intrd = "ѧ�������ס�ĵط�������17��֮��";
	G.vexs[2].name = "ʳ��"; G.vexs[2].code = '2'; G.vexs[2].intrd = "ѧ����ʦ�òͳ�������������¥��ÿһ�㶼�в�ͬ�����ṩ��ͬ�Ĳ���";
	G.vexs[3].name = "��ϢѧԺ"; G.vexs[3].code = '3'; G.vexs[3].intrd = "�йؼ����רҵ��ѧ���ϿΣ�ʵ��ĳ���";
	G.vexs[4].name = "ͼ���"; G.vexs[4].code = '4'; G.vexs[4].intrd = "ӵ�к������飬ѧ�������ڴ˵���ϰ";
	G.vexs[5].name = "�ĵ�¥"; G.vexs[5].code = '5'; G.vexs[5].intrd = "ѧ���ϿΣ���ʦ��ѧ�Ľ�ѧ¥֮һ";
	G.vexs[6].name = "��ɽ¥"; G.vexs[6].code = '6'; G.vexs[6].intrd = "ѧ���ϿΣ���ʦ��ѧ�Ľ�ѧ¥֮һ";
	G.vexs[7].name = "������"; G.vexs[7].code = '7'; G.vexs[7].intrd = "ѧ�������ڶ��������ĳ���";
	G.vexs[8].name = "�ٳ�"; G.vexs[8].code = '8'; G.vexs[8].intrd = "ѧ�������ڶ��������ν��е���Ҫ����";
	G.vexs[9].name = "�˽���"; G.vexs[9].code = '9'; G.vexs[9].intrd = "У԰��ɫ���㣬�ǽ�������־�Ծ���";
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
	cout << "    " << "��ӭ����У԰��ѯ����ϵͳ��" << endl;
	cout << "******************************" << endl;
	cout << endl;
}
void P2()
{
	cout << "   " << "������Ҫ��ѯ�ķ�����" << endl;
	cout << endl;
	cout << "   " << "��1��ѯ��ؾ������Ϣ" << endl;
	cout << "   " << "��2��ѯ���������·��" << endl;
}
void P3()
{
	cout << "  " << "0:����"<<endl;
	cout << "  " << "1:����"<<endl;
	cout << "  " << "2:ʳ��"<<endl;
	cout << "  " << "3:��ϢѧԺ"<<endl;
	cout << "  " << "4:ͼ���" << endl;;
	cout << "  " << "5:�ĵ�¥" << endl;
	cout << "  " << "6:��ɽ¥" << endl;
	cout << "  " << "7:������" << endl;
	cout << "  " << "8:�ٳ�" << endl;
	cout << "  " << "9:�˽���" << endl;
}
void serve(Sgraph& s, char n)
{
	for (int i = 0; i < s.vexnum; i++)
	{
		if (s.vexs[i].code == n)cout << s.vexs[i].name << "��" << s.vexs[i].intrd;
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
	push(S, v9); e = v9;     //����e������������ǰ��
	while (f1)               //f1����ѭ�������ж�
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
		el[f] = pop(S,e);     //el���������洢ջS������ֵ
		f++;
	}
	cout << "  " << "Ϊ���滮���·��:";
	for(int i=0;i<f;i++)
	{
	   cout<<G.vexs[el[i]].name<<" ";
	} 
	cout << endl;
	cout << endl;
	cout << G.vexs[v0].name << "��" << G.vexs[v9].name << "�����·��Ϊ��" << D[v9];
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
							cout << "   " << "������Ҫ��ѯ�ľ����ţ�" << endl;
							cout << endl;
							P3();
							P4();
							cin >> s2;
							if (s2 < '0' || s2>'9')
							{
								P4();
								cout << "   " << "��������ȷ�ı�ţ�" << endl;
								P4();
								break;
							}
							P4();
							serve(s, s2);
							P4();
							cout << "   " << "�Ƿ������ѯ�������㣿" << endl;
							cout << "   " << "Yes��Y" << "  " << "No��N" << endl;
							P4();
							cin >> s3;
							if (s3 == 'Y')t2 = 1;
							else if (s3 == 'N') t2 = 0;
							else
							{
								P4();
								cout << "  " << "�����ˣ��˳������ѯ" << endl;
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
							cout << "   " << "��������Ҫ��ѯ�����صı�ţ�" << endl;
							cout << endl;
							P3();
							P4();
							cin >> s4 >> s5;
							if ((s4 < 0 || s4>9) || (s5 < 0 || s5>9))
							{
								P4();
								cout << "   " << "��������ȷ�ı�ţ�" << endl;
								P4();
								break;
							}
							P4();
							Short(s, s4, s5);
							P4();
							cout << "   " << "�Ƿ������ѯ��" << endl;
							cout << "   " << "Yes��Y" << "  " << "No��N" << endl;
							P4();
							cin >> s3;
							if (s3 == 'Y')t2 = 1;
							else if (s3 == 'N') t2 = 0;
							else
							{
								P4();
								cout << "  " << "�����ˣ��˳�·����ѯ" << endl;
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
				cout << "   " << "��������ȷ����ţ�" << endl;
				P4();
				break;
			}
			P4();
			cout << "   " << "�Ƿ��˳���ѯϵͳ��" << endl;
			cout << "   " << "Yes��Y" << "  " << "No��N" << endl;
			P4();
			cin >> s6;
			if (s6 == 'Y')t = 0;
			if (s6 == 'N')t = 1;
			t2 = 1;
		}
	}
	P4();
	cout << "    " << "��л����ʹ��!�ټ�" << endl;
} 
