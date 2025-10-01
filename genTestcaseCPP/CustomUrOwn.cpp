#include <bits/stdc++.h>
using namespace std;

#define int long long
#define pii pair<int,int>
#define pcc pair<char,char>

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

int gen_number(const pii &limit){
    return generater(limit.first,limit.second);
}

vector<int> gen_vector_number(const pii &limit,const int &n,const bool &repeat){
    if(!repeat && limit.second-limit.first+1 < n){
        cout << "cannot generate cause out of range limit\n";
        return {};
    }
    vector<int> ans;
    if(repeat){
        multiset<int> ms;
        ms.insert(limit.first);
        ms.insert(limit.second);
        while(ms.size()!=n){
            ms.insert(generater(limit.first+1,limit.second-1));
        }
        for(auto &x:ms)ans.emplace_back(x);
    }else{
        set<int> s;
        s.insert(limit.first);
        s.insert(limit.second);
        while(s.size()!=n){
            s.insert(generater(limit.first+1,limit.second-1));
        }
        for(auto &x:s)ans.emplace_back(x); 
    }
    return ans;
}

vector<vector<int>> gen_matrix_number(const pii &limit,const int &n,const int &m,const bool &repeat){
    if(!repeat && limit.second-limit.first+1 < n*m){
        cout << "cannot generate cause out of range limit\n";
        return {{}};
    }
    vector<vector<int>> ans;
    if(repeat){
        unordered_multiset<int> ms;
        ms.insert(limit.first);
        ms.insert(limit.second);
        while(ms.size()!=n*m){
            ms.insert(generater(limit.first+1,limit.second-1));
        }
        int cnt=0;
        vector<int> tmp;
        for(auto &x:ms){
            tmp.emplace_back(x);
            cnt++;
            if(cnt==m){
                ans.emplace_back(tmp);
                tmp.clear();
                cnt=0;
            }
        }
    }else{
        unordered_set<int> s;
        s.insert(limit.first);
        s.insert(limit.second);
        while(s.size()!=n*m){
            s.insert(generater(limit.first+1,limit.second-1));
        }
        int cnt=0;
        vector<int> tmp;
        for(auto &x:s){
            tmp.emplace_back(x);
            cnt++;
            if(cnt==m){
                ans.emplace_back(tmp);
                tmp.clear();
                cnt=0;
            }
            
        }
    }
    return ans;
}

int gen_char(const pcc &limit){
    return generater((int)limit.first,(int)limit.second);
}

vector<char> gen_vector_char(const pcc &limit,const int &n,const bool &repeat){
    if(!repeat && limit.second-limit.first+1 < n){
        cout << "cannot generate cause out of range limit\n";
        return {};
    }
    vector<char> ans;
    if(repeat){
        multiset<char> ms;
        ms.insert(limit.first);
        ms.insert(limit.second);
        while(ms.size()!=n){
            ms.insert((char)generater((int)limit.first+1,(int)limit.second-1));
        }
        for(auto &x:ms)ans.emplace_back(x);
    }else{
        set<char> s;
        s.insert(limit.first);
        s.insert(limit.second);
        while(s.size()!=n){
            s.insert((char)generater((int)limit.first+1,(int)limit.second-1));
        }
        for(auto &x:s)ans.emplace_back(x);    
    }
    return ans;
}

vector<vector<char>> gen_matrix_char(const pcc &limit,const int &n,const int &m,const bool &repeat){
    if(!repeat && limit.second-limit.first+1 < n*m){
        cout << "cannot generate cause out of range limit\n";
        return {{}};
    }
    vector<vector<char>> ans;
    if(repeat){
        unordered_multiset<char> ms;
        ms.insert(limit.first);
        ms.insert(limit.second);
        while(ms.size()!=n*m){
            ms.insert(generater((int)limit.first+1,(int)limit.second-1));
        }
        int cnt=0;
        vector<char> tmp;
        for(auto &x:ms){
            tmp.emplace_back(x);
            cnt++;
            if(cnt==m){
                ans.emplace_back(tmp);
                tmp.clear();
                cnt=0;
            }
        }
    }else{
        unordered_set<char> s;
        s.insert(limit.first);
        s.insert(limit.second);
        while(s.size()!=n*m){
            s.insert(generater((int)limit.first+1,(int)limit.second-1));
        }
        int cnt=0;
        vector<char> tmp;
        for(auto &x:s){
            tmp.emplace_back(x);
            cnt++;
            if(cnt==m){
                ans.emplace_back(tmp);
                tmp.clear();
                cnt=0;
            }
            
        }
    }
    return ans;
}

string gen_word(const pcc &limit1,const pcc &limit2,const int &n){
    string ans = "";
    while(ans.size() != n){
        int mode = gen_number({0,1});
        if(mode){
            ans+=gen_char(limit1);
        }else{
            ans+=gen_char(limit2);
        }
    }
    return ans;
}

vector<string> gen_vector_word(const int &n,const int &min_size,const int &max_size,const bool &lower,const bool &upper,const bool &repeat){
    vector<string> ans;
    pcc limit1,limit2;
    if(lower)limit1 = {'a','z'};
    else limit1 = {'A','Z'};
    if(upper)limit2 = {'A','Z'};
    else limit2 = {'a','z'};
    if(repeat){
        unordered_multiset<string> ms;
        while(ms.size() != n){
            ms.insert(gen_word(limit1,limit2,gen_number({min_size,max_size})));
        }
        for(auto &x:ms)ans.emplace_back(x);
    }else{
        unordered_set<string> s;
        while(s.size() != n){
            s.insert(gen_word(limit1,limit2,gen_number({min_size,max_size})));
        }
        for(auto &x:s)ans.emplace_back(x);
    }
    return ans;
}

bool gen_boolean(){
    return gen_number({0,1});
}

vector<bool> gen_vector_boolean(const int &n){
    vector<bool> ans;
    while(ans.size() != n){
        ans.emplace_back(gen_boolean());
    }
    return ans;
}

vector<vector<bool>> gen_matrix_boolean(const int &n,const int &m){
    vector<vector<bool>> ans;
    int cnt=0;
    vector<bool> tmp;
    for(int i=0;i<n*m;i++){
        tmp.emplace_back(gen_boolean());
        cnt++;
        if(cnt==m){
            ans.emplace_back(tmp);
            cnt=0;
            tmp.clear();
        }
    }
    return ans;
}

void solve(){
    //edit your solution here;

}

void save_testcase(const string &name,const string &input,const string &output){
    writeFile(name,input,".in");
    writeFile(name,output,".sol");
}

int32_t main(){
    ios_base::sync_with_stdio(false);cin.tie(NULL);
    //it's up to you make you own!
    return 0;

}

