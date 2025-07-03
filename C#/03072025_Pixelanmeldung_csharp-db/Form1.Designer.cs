namespace _03072025_Pixelanmeldung_csharp_db
{
    partial class Form1
    {
        /// <summary>
        /// Erforderliche Designervariable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Verwendete Ressourcen bereinigen.
        /// </summary>
        /// <param name="disposing">True, wenn verwaltete Ressourcen gelöscht werden sollen; andernfalls False.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Vom Windows Form-Designer generierter Code

        /// <summary>
        /// Erforderliche Methode für die Designerunterstützung.
        /// Der Inhalt der Methode darf nicht mit dem Code-Editor geändert werden.
        /// </summary>
        private void InitializeComponent()
        {
            this.lb_name = new System.Windows.Forms.Label();
            this.lb_passwort = new System.Windows.Forms.Label();
            this.bn_Anmelung = new System.Windows.Forms.Button();
            this.tb_Name = new System.Windows.Forms.TextBox();
            this.tb_passwort = new System.Windows.Forms.TextBox();
            this.lb_ergebnis = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // lb_name
            // 
            this.lb_name.AutoSize = true;
            this.lb_name.Location = new System.Drawing.Point(34, 43);
            this.lb_name.Name = "lb_name";
            this.lb_name.Size = new System.Drawing.Size(51, 20);
            this.lb_name.TabIndex = 1;
            this.lb_name.Text = "Name";
            // 
            // lb_passwort
            // 
            this.lb_passwort.AutoSize = true;
            this.lb_passwort.Location = new System.Drawing.Point(38, 116);
            this.lb_passwort.Name = "lb_passwort";
            this.lb_passwort.Size = new System.Drawing.Size(78, 20);
            this.lb_passwort.TabIndex = 2;
            this.lb_passwort.Text = "Passwort:";
            // 
            // bn_Anmelung
            // 
            this.bn_Anmelung.Location = new System.Drawing.Point(474, 247);
            this.bn_Anmelung.Name = "bn_Anmelung";
            this.bn_Anmelung.Size = new System.Drawing.Size(96, 42);
            this.bn_Anmelung.TabIndex = 3;
            this.bn_Anmelung.Text = "Anmeldung";
            this.bn_Anmelung.UseVisualStyleBackColor = true;
            this.bn_Anmelung.Click += new System.EventHandler(this.button1_Click);
            // 
            // tb_Name
            // 
            this.tb_Name.Location = new System.Drawing.Point(155, 36);
            this.tb_Name.Name = "tb_Name";
            this.tb_Name.Size = new System.Drawing.Size(148, 26);
            this.tb_Name.TabIndex = 4;
            // 
            // tb_passwort
            // 
            this.tb_passwort.Location = new System.Drawing.Point(155, 113);
            this.tb_passwort.Name = "tb_passwort";
            this.tb_passwort.Size = new System.Drawing.Size(148, 26);
            this.tb_passwort.TabIndex = 5;
            // 
            // lb_ergebnis
            // 
            this.lb_ergebnis.AutoSize = true;
            this.lb_ergebnis.Location = new System.Drawing.Point(353, 382);
            this.lb_ergebnis.Name = "lb_ergebnis";
            this.lb_ergebnis.Size = new System.Drawing.Size(70, 20);
            this.lb_ergebnis.TabIndex = 6;
            this.lb_ergebnis.Text = "ergebnis";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.lb_ergebnis);
            this.Controls.Add(this.tb_passwort);
            this.Controls.Add(this.tb_Name);
            this.Controls.Add(this.bn_Anmelung);
            this.Controls.Add(this.lb_passwort);
            this.Controls.Add(this.lb_name);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lb_name;
        private System.Windows.Forms.Label lb_passwort;
        private System.Windows.Forms.Button bn_Anmelung;
        private System.Windows.Forms.TextBox tb_Name;
        private System.Windows.Forms.TextBox tb_passwort;
        private System.Windows.Forms.Label lb_ergebnis;
    }
}

