using System;
using System.Collections.Generic;
using System.Linq;
using System.Data.SQLite;

using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data;

namespace PoweroutageMap
{
    public partial class Googlemap : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            CreateConnection();
        }

        [System.Web.Services.WebMethod]
        public static string GetCurrentTime(string name)
        {
            return "Hello " + name + Environment.NewLine + "The Current Time is: "
                + DateTime.Now.ToString();
        }



        public  string CreateConnection() {

            SQLiteConnection sqlite_conn;
            String Path = @"C:\Users\dhava\PycharmProjects\DataCollectionPractical\poweroutages.sqlite";
            sqlite_conn = new SQLiteConnection("Data Source= " + Path);
            try
            {
                sqlite_conn.Open();
                DataSet DS = new DataSet();
                DataTable DT = new DataTable();
                SQLiteDataAdapter DB;
                // sqlite_cmd.CommandText = "SELECT * FROM NESOutagesDetails";
                string CommandText = "SELECT * FROM OutageDetail";
                DB = new SQLiteDataAdapter(CommandText, sqlite_conn);
                DS.Reset();
                DB.Fill(DS);
                DT = DS.Tables[0];

                System.Web.Script.Serialization.JavaScriptSerializer serializer = new System.Web.Script.Serialization.JavaScriptSerializer();
                List<Dictionary<string, object>> rows = new List<Dictionary<string, object>>();
                Dictionary<string, object> row;
                foreach (DataRow dr in DT.Rows)
                {
                    row = new Dictionary<string, object>();
                    foreach (DataColumn col in DT.Columns)
                    {
                        row.Add(col.ColumnName, dr[col]);
                    }
                    rows.Add(row);
                }
                 sqlite_conn.Close();
                return serializer.Serialize(rows);
            }
            catch (Exception ex)
            {

            }

            return "";

        }


        

    }



}




    
