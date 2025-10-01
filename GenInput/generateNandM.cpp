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

vector<pii> gen(const pii limit_N,const pii limit_M,const int n){
    set<pii> s;
    s.insert({limit_N.first,limit_M.first});
    s.insert({limit_N.first,limit_M.second});
    s.insert({limit_N.second,limit_M.first});
    s.insert({limit_N.second,limit_M.second});
    while(s.size() != n){
        s.insert({generater(limit_N.first+1,limit_N.second-1),generater(limit_M.first+1,limit_M.second-1)});
    }
    vector<pii> v;
    for(auto &x:s)v.emplace_back(x);
    return v;
}

int solve(int &n,int &m){
    //edit your solution here;
    
    return 0;
}

int32_t main(){
    ios_base::sync_with_stdio(false);cin.tie(NULL);
    int min_N = 0;//minimum of n
    int max_N = 40;//maximum of n
    int min_M = 0;//minimum of m
    int max_M = 40;//maximum of m
    int testcase = 5;//number of testcase
    vector<pii> v = gen({min_N,max_N},{min_M,max_M},testcase);
    for(int i=0;i<v.size();i++){
        string name=to_string(i+1);
        string input=(to_string(v[i].first)+" "+to_string(v[i].second));
        string output=to_string(solve(v[i].first,v[i].second));
        writeFile(name,input,".in");
        writeFile(name,output,".sol");
    }
    return 0;
}