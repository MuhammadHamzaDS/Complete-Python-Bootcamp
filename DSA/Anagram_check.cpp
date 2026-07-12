#include<iostream>
using namespace std;

int main()
{
    string a = "listen";
    string b = "silent";

    int count1[26] = {0};
    int count2[26] = {0};

    for(int i=0; i<a.length(); i++)
    {
        count1[a[i]-'a']++;
    }

    for(int i=0; i<b.length(); i++)
    {
        count2[b[i]-'a']++;
    }

    bool isAnagram = true;

    for(int i=0; i<26; i++)
    {
        if(count1[i] != count2[i])
        {
            isAnagram = false;
            break;
        }
    }

    if(isAnagram)
        cout<<"Anagram";
    else
        cout<<"Not Anagram";

    return 0;
}