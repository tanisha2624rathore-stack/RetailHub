from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.db import connection

class add_purchase(APIView):
    def post(self,request,id=None):
        company_name=request.data.get("company_name")
        product_name=request.data.get("product_name")
        price=request.data.get("price")
        qty=request.data.get("qty")
        total_price=request.data.get("total_price")
        cursor=connection.cursor()   
        if id is None:
            try:
                result=cursor.execute("insert into service_purchase_detail(company_name,product_name,qty,price,total_price,`delete`)values(%s,%s,%s,%s,%s,%s) ",[company_name,product_name,qty,price,total_price,"N"])
                print("result",result)
                cursor.close()
                return Response({
                    "message":"data add sucessful"
                })
            except Exception as e:
                print("error",e)
        else:
            print("update id",id)
            cursor.execute(f""" update service_Purchase_detail set company_name=%s,product_name=%s,
            qty=%s,price=%s,total_price=%s where id=%s and `delete`=%s """,[company_name,product_name,qty,price,total_price,id,"N"])
            print("message data update successfuly")
            return Response({"message":"data update successfuly"})

    def get(self,request,id):
        id=id
        print("api id",id)
        cursor=connection.cursor()
        try:
            cursor.execute("select id, company_name, product_name, qty,price,total_price from service_Purchase_detail where id=%s and `delete`=%s",[id,"N"])
            columns = [col[0] for col in cursor.description]
            rows=cursor.fetchall()
            result = []
        
            for row in rows:
                result.append(dict(zip(columns, row)))
                print("row",row)
    
            cursor.close()
        
            return Response({"result": result})
        except Exception as e:
            print("error",e)
            return Response({"message": "error"})

class purchase_list_api(APIView):
    def get(self,request):
        cursor=connection.cursor()
        cursor.execute("select id ,company_name,product_name,price,qty,total_price from service_purchase_detail where `delete`='N'")
        columns = [col[0] for col in cursor.description]
        rows=cursor.fetchall()
        result = []

        for row in rows:
            result.append(dict(zip(columns, row)))
           

        cursor.close()

        return Response({"result": result})

class delete_purchase_api(APIView):
    def get(self,request,id):
        print("delete id",id)
        cursor=connection.cursor()
        cursor.execute("update service_Purchase_detail set `delete`='Y' where id=%s",[id])
        print("data deleted successfuly")
        return Response({
            "massage":"data deleted successfuly"
        }) 
       
class filter_purchase_api(APIView):
    def get(self,request):
        data_value=request.data.get("search_value")
        print(data_value)
        cursor=connection.cursor()
        p_list=[]
        query=("select company_name,product_name,qty,price, total_price from service_Purchase_detail where 1=1")
        if data_value:
            query+=f""" AND (company_name LIKE %s OR product_name LIKE %s OR CAST(qty as CHAR)LIKE %s OR CAST(price as CHAR) LIKE %s)"""

            search=f"%{data_value}%"
            p_list.extend([search,search,search,search])
            cursor.execute(query,p_list)
            data=cursor.fetchall()
            print("data ====",data)
            return Response({
                "data":data

            })





       


        

    
        
            



