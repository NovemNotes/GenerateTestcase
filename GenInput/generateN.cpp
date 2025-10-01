#include <bits/stdc++.h>
using namespace std;

#define int long long
#define pii pair<int,int>

void writeFile(const string &name,const string &content,const string &surname){
    ofstream fout(name+surname);
    if(!fout)cout << "cannot write file " << name << " " << "." << surname << "\n";;
    fout << content << "\n";
    fout.close();
}

int generater(const int mn,const int mx){
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> distrib(mn, mx);
    int random=distrib(gen);
    return random;
}

vector<int> gen(const pii limit,const int n){
    set<int> s;
    s.insert(limit.first);
    s.insert(limit.second);
    while(s.size() != n){
        s.insert(generater(limit.first+1,limit.second-1));
    }
    vector<int> v;
    for(auto &x:s)v.emplace_back(x);
    return v;
}

int solve(int n){
    
}

int32_t main(){
    ios_base::sync_with_stdio(false);cin.tie(NULL);
    int min_N = 0;//minimum of n
    int max_N = 40;//maximum of n
    int testcase = 5;//number of testcase
    vector<int> v = gen({min_N,max_N},testcase);
    for(int i=0;i<v.size();i++){
        string name=to_string(i+1);
        string input=to_string(v[i]);
        string output=to_string(solve(v[i]));
        writeFile(name,input,".in");
        writeFile(name,output,".sol");
    }
    return 0;
}