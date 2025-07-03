using System.Security.Cryptography;
using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;



namespace _03072025_Pixelanmeldung_csharp_db
{
     
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            
        }
        string name;
        string passwort;
        



        private void button1_Click(object sender, EventArgs e)
        {
            name = tb_Name.Text;
            passwort = tb_passwort.Text;

            var dbConnection = new MariaDbConnection();
            bool loginErfolgreich = dbConnection.ValidateLogin(name, passwort);

            if (loginErfolgreich)
            {
                lb_ergebnis.Text = "Erfolgreich eingeloggt";
                lb_ergebnis.ForeColor = Color.Green;
            }
            else
            {
                lb_ergebnis.Text = "Falscher Benutzername oder Passwort";
                lb_ergebnis.ForeColor = Color.Red;
            }

        }
    }


    public class MariaDbConnection
    {
        private string connectionString = "Server=10.80.0.206;Port=3306;Database=team09;User ID=team09;Password=NHHJS;";

        public bool ValidateLogin(string username, string password)
        {
            

            using (var connection = new MySqlConnection(connectionString))
            {
                try
                {
                    connection.Open();
                    string sql = "SELECT COUNT(*) FROM Spieler WHERE BINARY Benutzername = @username AND BINARY Passwort = @password";



                    using (var command = new MySqlCommand(sql, connection))
                    {
                        // Parameterisiertes Query für Sicherheit
                        command.Parameters.AddWithValue("@username", username);
                        command.Parameters.AddWithValue("@password", password);

                        int count = Convert.ToInt32(command.ExecuteScalar());
                        return count > 0;
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Datenbankfehler: {ex.Message}");
                    return false;
                }
            }
        }

        
    }

    
}
