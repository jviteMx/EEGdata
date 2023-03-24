// <-- EXPAND to see the data classes
import java.io.*;
import java.util.*;
import org.json.simple.parser.JSONParser;
import org.json.simple.JSONObject;
import org.json.simple.JSONArray;

class PositiveReview {
    Integer userId;
    Integer businessId;

    public PositiveReview(Integer userId, Integer businessId) {
        this.userId = userId;
        this.businessId = businessId;
    }

    public Integer getUserId() {
        return this.userId;
    }
    public Integer getBusinessId() {
        return this.businessId;
    }
}

class Solution {

    /*
    Sample Input
        {
            "businessOfInterestId": 10,
            "positiveReviews": [
                PositiveReview(
                    "userId": 1,
                    "businessId": 10
                ),
                PositiveReview(
                    "userId": 2,
                    "businessId": 10
                ),
                PositiveReview(
                    "userId": 1,
                    "businessId": 11
                ),
                PositiveReview(
                    "userId": 2,
                    "businessId": 11
                ),
                PositiveReview(
                    "userId": 1,
                    "businessId": 12
                ),
                PositiveReview(
                    "userId": 2,
                    "businessId": 12
                ),
                PositiveReview(
                    "userId": 3,
                    "businessId": 12
                )
            ]
        }
    Sample Output
        11
    Business Similarity Score against business 10:
        11: 2 / (2 + 2 - 2) = 1.0
        12: 2 / (2 + 3 - 2) = 0.667
    */
    public static Integer findMostSimilarBusiness(
        Integer businessOfInterestId,
        List<PositiveReview> positiveReviews) 
        {
            Map<Integer,List<Integer>>jk=new HashMap<>();
            for (int i=0;i<positiveReviews.size();i++){
                if (jk.containsKey(positiveReviews.get(i).businessId)){
                List<Integer>result=jk.get(positiveReviews.get(i).businessId);
                result.add(positiveReviews.get(i).userId);
                jk.put(positiveReviews.get(i).businessId,result);
                }
                else{
                    List<Integer>numb=new ArrayList<>();
                    numb.add(positiveReviews.get(i).userId);
                    jk.put(positiveReviews.get(i).businessId,numb);
                }
            
                
            }
             List<Integer>BID_List=jk.get(businessOfInterestId);
             float max_sim=Float.NEGATIVE_INFINITY;
             int max_BID=-1;
             
             long i=0;
             for(Map.Entry<Integer,List<Integer>>pair:jk.entrySet()){
                 if(pair.getKey()!=businessOfInterestId){
                     float sim = (float)BID_List.stream().filter(pair.getValue()::contains).collect(Collector.toList()).size()/
                      (float)Stream.concat(BID_List.stream(),pair.getValue().stream()).distinct().collect(Collector.toList()).size);
                     if(sim>max_sim){
                         max_sim=sim;
                         max_BID=pair.getKey();
                     }
                 }
             }
        }
       

    public static void main(String[] args) {