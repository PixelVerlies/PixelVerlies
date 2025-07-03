namespace Projekt_DB_20250307
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
            this.rb_abfragen = new System.Windows.Forms.RadioButton();
            this.rb_anlegen = new System.Windows.Forms.RadioButton();
            this.bn_abfragen = new System.Windows.Forms.Button();
            this.rb_name = new System.Windows.Forms.RadioButton();
            this.rb_wuer = new System.Windows.Forms.RadioButton();
            this.rb_leb = new System.Windows.Forms.RadioButton();
            this.rb_vor = new System.Windows.Forms.RadioButton();
            this.rb_rueck = new System.Windows.Forms.RadioButton();
            this.gb_spalte = new System.Windows.Forms.GroupBox();
            this.gb_sort = new System.Windows.Forms.GroupBox();
            this.lib_anzeigen = new System.Windows.Forms.ListBox();
            this.tb_name = new System.Windows.Forms.TextBox();
            this.rb_bewegung = new System.Windows.Forms.RadioButton();
            this.lb_name = new System.Windows.Forms.Label();
            this.lb_wurfel = new System.Windows.Forms.Label();
            this.lb_bewegung = new System.Windows.Forms.Label();
            this.lb_leben = new System.Windows.Forms.Label();
            this.nup_wuerfel = new System.Windows.Forms.NumericUpDown();
            this.nup_bewegung = new System.Windows.Forms.NumericUpDown();
            this.nup_leben = new System.Windows.Forms.NumericUpDown();
            this.gb_anlegen = new System.Windows.Forms.GroupBox();
            this.gb_spalte.SuspendLayout();
            this.gb_sort.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nup_wuerfel)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nup_bewegung)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nup_leben)).BeginInit();
            this.gb_anlegen.SuspendLayout();
            this.SuspendLayout();
            // 
            // rb_abfragen
            // 
            this.rb_abfragen.AutoSize = true;
            this.rb_abfragen.Checked = true;
            this.rb_abfragen.Location = new System.Drawing.Point(551, 37);
            this.rb_abfragen.Name = "rb_abfragen";
            this.rb_abfragen.Size = new System.Drawing.Size(100, 24);
            this.rb_abfragen.TabIndex = 0;
            this.rb_abfragen.TabStop = true;
            this.rb_abfragen.Text = "Abfragen";
            this.rb_abfragen.UseVisualStyleBackColor = true;
            this.rb_abfragen.CheckedChanged += new System.EventHandler(this.rb_abfragen_CheckedChanged);
            // 
            // rb_anlegen
            // 
            this.rb_anlegen.AutoSize = true;
            this.rb_anlegen.Location = new System.Drawing.Point(551, 77);
            this.rb_anlegen.Name = "rb_anlegen";
            this.rb_anlegen.Size = new System.Drawing.Size(93, 24);
            this.rb_anlegen.TabIndex = 1;
            this.rb_anlegen.Text = "Anlegen";
            this.rb_anlegen.UseVisualStyleBackColor = true;
            this.rb_anlegen.CheckedChanged += new System.EventHandler(this.rb_anlegen_CheckedChanged);
            // 
            // bn_abfragen
            // 
            this.bn_abfragen.Location = new System.Drawing.Point(547, 458);
            this.bn_abfragen.Name = "bn_abfragen";
            this.bn_abfragen.Size = new System.Drawing.Size(117, 33);
            this.bn_abfragen.TabIndex = 2;
            this.bn_abfragen.Text = "Abfragen";
            this.bn_abfragen.UseVisualStyleBackColor = true;
            this.bn_abfragen.Click += new System.EventHandler(this.bn_abfragen_Click);
            // 
            // rb_name
            // 
            this.rb_name.AutoSize = true;
            this.rb_name.Checked = true;
            this.rb_name.Location = new System.Drawing.Point(14, 25);
            this.rb_name.Name = "rb_name";
            this.rb_name.Size = new System.Drawing.Size(76, 24);
            this.rb_name.TabIndex = 3;
            this.rb_name.TabStop = true;
            this.rb_name.Text = "Name";
            this.rb_name.UseVisualStyleBackColor = true;
            // 
            // rb_wuer
            // 
            this.rb_wuer.AutoSize = true;
            this.rb_wuer.Location = new System.Drawing.Point(14, 54);
            this.rb_wuer.Name = "rb_wuer";
            this.rb_wuer.Size = new System.Drawing.Size(80, 24);
            this.rb_wuer.TabIndex = 4;
            this.rb_wuer.Text = "Würfel";
            this.rb_wuer.UseVisualStyleBackColor = true;
            // 
            // rb_leb
            // 
            this.rb_leb.AutoSize = true;
            this.rb_leb.Location = new System.Drawing.Point(14, 84);
            this.rb_leb.Name = "rb_leb";
            this.rb_leb.Size = new System.Drawing.Size(79, 24);
            this.rb_leb.TabIndex = 5;
            this.rb_leb.Text = "Leben";
            this.rb_leb.UseVisualStyleBackColor = true;
            // 
            // rb_vor
            // 
            this.rb_vor.AutoSize = true;
            this.rb_vor.Checked = true;
            this.rb_vor.Location = new System.Drawing.Point(14, 29);
            this.rb_vor.Name = "rb_vor";
            this.rb_vor.Size = new System.Drawing.Size(97, 24);
            this.rb_vor.TabIndex = 6;
            this.rb_vor.TabStop = true;
            this.rb_vor.Text = "Vorwärts";
            this.rb_vor.UseVisualStyleBackColor = true;
            // 
            // rb_rueck
            // 
            this.rb_rueck.AutoSize = true;
            this.rb_rueck.Location = new System.Drawing.Point(14, 60);
            this.rb_rueck.Name = "rb_rueck";
            this.rb_rueck.Size = new System.Drawing.Size(109, 24);
            this.rb_rueck.TabIndex = 7;
            this.rb_rueck.Text = "Rückwärts";
            this.rb_rueck.UseVisualStyleBackColor = true;
            // 
            // gb_spalte
            // 
            this.gb_spalte.Controls.Add(this.rb_bewegung);
            this.gb_spalte.Controls.Add(this.rb_leb);
            this.gb_spalte.Controls.Add(this.rb_wuer);
            this.gb_spalte.Controls.Add(this.rb_name);
            this.gb_spalte.Location = new System.Drawing.Point(533, 145);
            this.gb_spalte.Name = "gb_spalte";
            this.gb_spalte.Size = new System.Drawing.Size(166, 153);
            this.gb_spalte.TabIndex = 8;
            this.gb_spalte.TabStop = false;
            this.gb_spalte.Text = "Spalte";
            // 
            // gb_sort
            // 
            this.gb_sort.Controls.Add(this.rb_rueck);
            this.gb_sort.Controls.Add(this.rb_vor);
            this.gb_sort.Location = new System.Drawing.Point(533, 330);
            this.gb_sort.Name = "gb_sort";
            this.gb_sort.Size = new System.Drawing.Size(166, 101);
            this.gb_sort.TabIndex = 9;
            this.gb_sort.TabStop = false;
            this.gb_sort.Text = "Sortierung";
            // 
            // lib_anzeigen
            // 
            this.lib_anzeigen.FormattingEnabled = true;
            this.lib_anzeigen.ItemHeight = 20;
            this.lib_anzeigen.Location = new System.Drawing.Point(94, 272);
            this.lib_anzeigen.Name = "lib_anzeigen";
            this.lib_anzeigen.Size = new System.Drawing.Size(345, 184);
            this.lib_anzeigen.TabIndex = 10;
            // 
            // tb_name
            // 
            this.tb_name.Location = new System.Drawing.Point(31, 57);
            this.tb_name.Name = "tb_name";
            this.tb_name.Size = new System.Drawing.Size(100, 26);
            this.tb_name.TabIndex = 11;
            // 
            // rb_bewegung
            // 
            this.rb_bewegung.AutoSize = true;
            this.rb_bewegung.Location = new System.Drawing.Point(14, 114);
            this.rb_bewegung.Name = "rb_bewegung";
            this.rb_bewegung.Size = new System.Drawing.Size(110, 24);
            this.rb_bewegung.TabIndex = 6;
            this.rb_bewegung.TabStop = true;
            this.rb_bewegung.Text = "Bewegung";
            this.rb_bewegung.UseVisualStyleBackColor = true;
            // 
            // lb_name
            // 
            this.lb_name.AutoSize = true;
            this.lb_name.Location = new System.Drawing.Point(27, 31);
            this.lb_name.Name = "lb_name";
            this.lb_name.Size = new System.Drawing.Size(51, 20);
            this.lb_name.TabIndex = 13;
            this.lb_name.Text = "Name";
            // 
            // lb_wurfel
            // 
            this.lb_wurfel.AutoSize = true;
            this.lb_wurfel.Location = new System.Drawing.Point(27, 110);
            this.lb_wurfel.Name = "lb_wurfel";
            this.lb_wurfel.Size = new System.Drawing.Size(55, 20);
            this.lb_wurfel.TabIndex = 14;
            this.lb_wurfel.Text = "Würfel";
            // 
            // lb_bewegung
            // 
            this.lb_bewegung.AutoSize = true;
            this.lb_bewegung.Location = new System.Drawing.Point(157, 109);
            this.lb_bewegung.Name = "lb_bewegung";
            this.lb_bewegung.Size = new System.Drawing.Size(85, 20);
            this.lb_bewegung.TabIndex = 17;
            this.lb_bewegung.Text = "Bewegung";
            // 
            // lb_leben
            // 
            this.lb_leben.AutoSize = true;
            this.lb_leben.Location = new System.Drawing.Point(157, 31);
            this.lb_leben.Name = "lb_leben";
            this.lb_leben.Size = new System.Drawing.Size(54, 20);
            this.lb_leben.TabIndex = 18;
            this.lb_leben.Text = "Leben";
            // 
            // nup_wuerfel
            // 
            this.nup_wuerfel.Location = new System.Drawing.Point(27, 134);
            this.nup_wuerfel.Maximum = new decimal(new int[] {
            6,
            0,
            0,
            0});
            this.nup_wuerfel.Name = "nup_wuerfel";
            this.nup_wuerfel.Size = new System.Drawing.Size(100, 26);
            this.nup_wuerfel.TabIndex = 19;
            // 
            // nup_bewegung
            // 
            this.nup_bewegung.Location = new System.Drawing.Point(161, 133);
            this.nup_bewegung.Name = "nup_bewegung";
            this.nup_bewegung.Size = new System.Drawing.Size(96, 26);
            this.nup_bewegung.TabIndex = 20;
            // 
            // nup_leben
            // 
            this.nup_leben.Location = new System.Drawing.Point(161, 59);
            this.nup_leben.Name = "nup_leben";
            this.nup_leben.Size = new System.Drawing.Size(96, 26);
            this.nup_leben.TabIndex = 21;
            // 
            // gb_anlegen
            // 
            this.gb_anlegen.Controls.Add(this.nup_leben);
            this.gb_anlegen.Controls.Add(this.nup_bewegung);
            this.gb_anlegen.Controls.Add(this.nup_wuerfel);
            this.gb_anlegen.Controls.Add(this.lb_leben);
            this.gb_anlegen.Controls.Add(this.lb_bewegung);
            this.gb_anlegen.Controls.Add(this.lb_wurfel);
            this.gb_anlegen.Controls.Add(this.lb_name);
            this.gb_anlegen.Controls.Add(this.tb_name);
            this.gb_anlegen.Enabled = false;
            this.gb_anlegen.Location = new System.Drawing.Point(94, 37);
            this.gb_anlegen.Name = "gb_anlegen";
            this.gb_anlegen.Size = new System.Drawing.Size(312, 207);
            this.gb_anlegen.TabIndex = 22;
            this.gb_anlegen.TabStop = false;
            this.gb_anlegen.Text = "Anlege Daten";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(754, 515);
            this.Controls.Add(this.gb_anlegen);
            this.Controls.Add(this.lib_anzeigen);
            this.Controls.Add(this.gb_sort);
            this.Controls.Add(this.gb_spalte);
            this.Controls.Add(this.bn_abfragen);
            this.Controls.Add(this.rb_anlegen);
            this.Controls.Add(this.rb_abfragen);
            this.Name = "Form1";
            this.Text = "Form1";
            this.gb_spalte.ResumeLayout(false);
            this.gb_spalte.PerformLayout();
            this.gb_sort.ResumeLayout(false);
            this.gb_sort.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nup_wuerfel)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nup_bewegung)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nup_leben)).EndInit();
            this.gb_anlegen.ResumeLayout(false);
            this.gb_anlegen.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RadioButton rb_abfragen;
        private System.Windows.Forms.RadioButton rb_anlegen;
        private System.Windows.Forms.Button bn_abfragen;
        private System.Windows.Forms.RadioButton rb_name;
        private System.Windows.Forms.RadioButton rb_wuer;
        private System.Windows.Forms.RadioButton rb_leb;
        private System.Windows.Forms.RadioButton rb_vor;
        private System.Windows.Forms.RadioButton rb_rueck;
        private System.Windows.Forms.GroupBox gb_spalte;
        private System.Windows.Forms.GroupBox gb_sort;
        private System.Windows.Forms.ListBox lib_anzeigen;
        private System.Windows.Forms.TextBox tb_name;
        private System.Windows.Forms.RadioButton rb_bewegung;
        private System.Windows.Forms.Label lb_name;
        private System.Windows.Forms.Label lb_wurfel;
        private System.Windows.Forms.Label lb_bewegung;
        private System.Windows.Forms.Label lb_leben;
        private System.Windows.Forms.NumericUpDown nup_wuerfel;
        private System.Windows.Forms.NumericUpDown nup_bewegung;
        private System.Windows.Forms.NumericUpDown nup_leben;
        private System.Windows.Forms.GroupBox gb_anlegen;
    }
}

