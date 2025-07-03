using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml.Linq;
using MySql.Data.MySqlClient;
using Mysqlx.Crud;

namespace Projekt_DB_20250307
{
    public partial class Form1: Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void bn_abfragen_Click(object sender, EventArgs e)
        {
            lib_anzeigen.Items.Clear();

            MySqlConnection connection = new MySqlConnection("server=10.80.0.206;database=team09;uid=team09;password=NHHJS");

            connection.Open();

            if (rb_abfragen.Checked)
            {
                string sortBy = "";
                string sortOrder = "";

                if (rb_name.Checked == true)
                {
                    sortBy = "Gegner.Name";
                }
                else if (rb_wuer.Checked == true)
                {
                    sortBy = "Wuerfel.Seiten";
                }
                else if (rb_bewegung.Checked == true)
                {
                    sortBy = "Gegner.Bewgeungsrate";
                }
                else
                {
                    sortBy = "Gegner.LP";
                }

                if (rb_vor.Checked == true)
                {
                    sortOrder = "ASC";
                }
                else
                {
                    sortOrder = "DESC";
                }

                string sql = "SELECT Gegner.Name, Gegner.LP, Wuerfel.seiten, Gegner.Bewgeungsrate FROM Gegner JOIN Wuerfel ON Gegner.wuerfelID = Wuerfel.wuerfelID ORDER BY " + sortBy + " " + sortOrder;
                MySqlCommand cmd = new MySqlCommand(sql, connection);
                MySqlDataReader rdr = cmd.ExecuteReader();

                lib_anzeigen.Items.Add("Name\tWürfel\tLeben");


                while (rdr.Read())
                {
                    lib_anzeigen.Items.Add($"{rdr[0]}\t{rdr[1]}\t{rdr[2]}");
                }
            }
            else
            {
                string name = "";
                int lp = 0;
                int wuerfel = 0;
                int bewegung = 0;

                name = tb_name.Text;
                lp = Convert.ToInt32(nup_leben.Value);
                wuerfel = Convert.ToInt32(nup_wuerfel.Value);
                bewegung = Convert.ToInt32(nup_bewegung.Value);

                MySqlCommand comm = connection.CreateCommand();
                comm.CommandText = "INSERT INTO Gegner (Name, WuerfelID, LP, Bewgeungsrate) VALUES(\"" + name + "\", " + wuerfel + ", " + lp + ", " + bewegung + ")";
                comm.ExecuteNonQuery();

                tb_name.ResetText();
                nup_leben.ResetText();
                nup_wuerfel.ResetText();
                nup_bewegung.ResetText();
            }

            connection.Close();
        }

        private void rb_abfragen_CheckedChanged(object sender, EventArgs e)
        {
            gb_sort.Enabled = true;
            gb_spalte.Enabled = true;
            lib_anzeigen.Enabled = true;
            gb_anlegen.Enabled = false;
            bn_abfragen.Text = "Abfragen";
        }

        private void rb_anlegen_CheckedChanged(object sender, EventArgs e)
        {
            gb_sort.Enabled = false;
            gb_spalte.Enabled = false;
            lib_anzeigen.Enabled = false;
            gb_anlegen.Enabled = true;
            bn_abfragen.Text = "Anlegen";
        }
    }
}
