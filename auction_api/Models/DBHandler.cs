using System;
using System.Collections.Generic;
using System.Web;
using Npgsql;
using System.Configuration;

namespace auction_api.Models
{
    public class DBHandler
    {
        
        public List<Auction> GetAllAuctions()
        {
            string cmdText = "SELECT * FROM kvd_auction_object";
            List<Auction> auctionlist = new List<Auction>();

            using (var connection = new NpgsqlConnection(ConfigurationManager.ConnectionStrings["PostgreSQL"].ConnectionString))
            {
                connection.Open();

                using (var cmd = new NpgsqlCommand(cmdText, connection))
                {
                    using (var reader = cmd.ExecuteReader())
                    {
                        while(reader.Read())
                        {
                            var auction = new Auction();
                            auction.ObjectNumber = reader.GetInt32(0);
                            auction.CarModel = GetSafeString(reader, 2);
                            auctionlist.Add(auction);
                        }
                    }
                }
                 
            }
            return auctionlist;
        }

        public Auction GetAuctionByObjectNumber(int objectnumber)
        {
            string cmdText = "select * from kvd_auction_object where object_number =" + objectnumber.ToString();
            
            using (var connection = new NpgsqlConnection(ConfigurationManager.ConnectionStrings["PostgreSQL"].ConnectionString))
            {
                connection.Open();

                using (var cmd = new NpgsqlCommand(cmdText, connection))
                {
                    using (var reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            var auction = new Auction();
                            auction.ObjectNumber = reader.GetInt32(0);
                            auction.CarModel = reader.GetString(2);
                            return auction;
                        }
                    }
                }

            }
            return null;
        }

        private string GetSafeString(NpgsqlDataReader reader, int colindex)
        {
            if(reader.IsDBNull(colindex))
            {
                return string.Empty;
            }
            else
            {
                return reader.GetString(colindex);
            }
        }
    }
}