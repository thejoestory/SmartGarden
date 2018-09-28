    [WebMethod]
    public string LogMoisture(string sensorID, string reading) {
        SqlConnection con = new SqlConnection(@"Data Source=SERVER;Initial Catalog=databaseName;Integrated Security=true;");
        SqlCommand cmd = new SqlCommand(@"EXECUTE smart_garden_LogMoisture @sensorID='" + sensorID + "',@reading='" + reading + "'", con);
        con.Open();

        try
        {
            int i = cmd.ExecuteNonQuery();
            con.Close();
            return "Data Logged: " + i.ToString();
        }
        catch (Exception e)
        {
            return "Failed" + e.ToString();
        }

    }

    [WebMethod]
    public string LogTemp(string sensorID, string temp, string humidity)
    {
        SqlConnection con = new SqlConnection(@"Data Source=SERVER;Initial Catalog=databaseName;Integrated Security=true;");
        SqlCommand cmd = new SqlCommand(@"EXECUTE smart_garden_LogTemp @sensorID='" + sensorID + "',@temp='" + temp + "',@humidity='" + humidity + "'", con);
        con.Open();

        try
        {
            int i = cmd.ExecuteNonQuery();
            con.Close();
            return "Data Logged: " + i.ToString();
        }
        catch (Exception e)
        {
            return "Failed" + e.ToString();
        }

    }

    [WebMethod]
    public string LogLight(string sensorID, string reading)
    {
        SqlConnection con = new SqlConnection(@"Data Source=SERVER;Initial Catalog=databaseName;Integrated Security=true;");
        SqlCommand cmd = new SqlCommand(@"EXECUTE smart_garden_LogLight @sensorID='" + sensorID + "',@reading='" + reading + "'", con);
        con.Open();

        try
        {
            int i = cmd.ExecuteNonQuery();
            con.Close();
            return "Data Logged: " + i.ToString();
        }
        catch (Exception e)
        {
            return "Failed" + e.ToString();
        }

    }
