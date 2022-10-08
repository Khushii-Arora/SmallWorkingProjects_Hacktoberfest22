// Java program to write a student
// information in JFrame and
// storing it in a file

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class STUDENT_REGISTRATION_FORM {

    // Function to write a student
    // information in JFrame and
    // storing it in a file
    public static void StudentInfo()
    {

        // Creating a new frame using JFrame
        JFrame f
            = new JFrame(
                "Student Details Form");

        // Creating the labels
        JLabel l1, l2, l3, l4, l5;

        // Creating three text fields.
        // One for student name, one for
        // college mail ID and one
        // for Mobile No
        JTextField t1, t2, t3;

        // Creating two JComboboxes
        // one for Branch and one
        // for Section
        JComboBox j1, j2;

        // Creating two buttons
        JButton b1, b2;

        // Naming the labels and setting
        // the bounds for the labels
        l1 = new JLabel("Student Name:");
        l1.setBounds(50, 50, 100, 30);
        l2 = new JLabel("College Email ID:");
        l2.setBounds(50, 120, 120, 30);
        l3 = new JLabel("Branch:");
        l3.setBounds(50, 190, 50, 30);
        l4 = new JLabel("Section:");
        l4.setBounds(420, 50, 70, 30);
        l5 = new JLabel("Mobile No:");
        l5.setBounds(420, 120, 70, 30);

        // Creating the textfields and
        // setting the bounds for textfields
        t1 = new JTextField();
        t1.setBounds(150, 50, 130, 30);
        t2 = new JTextField();
        t2.setBounds(160, 120, 130, 30);
        t3 = new JTextField();
        t3.setBounds(490, 120, 130, 30);

        // Creating two string arrays one for
        // braches and other for sections
        String s1[]
            = { " ", "CSE", "ECE", "EEE",
                "CIVIL", "MEC", "Others" };
        String s2[]
            = { " ", "Section-A", "Section-B",
                "Section-C", "Section-D",
                "Section-E" };

        // Creating two JComboBoxes one for
        // selecting branch and other for
        // selecting the section
        // and setting the bounds
        j1 = new JComboBox(s1);
        j1.setBounds(120, 190, 100, 30);
        j2 = new JComboBox(s2);
        j2.setBounds(470, 50, 140, 30);

        // Creating one button for Saving
        // and other button to close
        // and setting the bounds
        b1 = new JButton("Save");
        b1.setBounds(150, 300, 70, 30);
        b2 = new JButton("close");
        b2.setBounds(420, 300, 70, 30);

        // Adding action listener
        b1.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e)
            {

                // Getting the text from text fields
                // and JComboboxes
                // and copying it to a strings

                String s1 = t1.getText();
                String s2 = t2.getText();
                String s3 = j1.getSelectedItem() + "";
                String s4 = j2.getSelectedItem() + "";
                String s5 = t3.getText();
                if (e.getSource() == b1) {
                    try {

                        // Creating a file and
                        // writing the data
                        // into a Textfile.
                        FileWriter w
                            = new FileWriter(
                                "SREYA.txt", true);

                        w.write(s1 + "\n");
                        w.write(s2 + "\n");
                        w.write(s3 + "\n");
                        w.write(s4 + "\n");
                        w.write(s5 + "\n");
                        w.close();
                    }
                    catch (Exception ae) {
                        System.out.println(ae);
                    }
                }

                // Shows a Pop up Message when
                // save button is clicked
                JOptionPane
                    .showMessageDialog(
                        f,
                        "Successfully Saved"
                            + " The Details");
            }
        });

        // Action listener to close the form
        b2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e)
            {
                f.dispose();
            }
        });

        // Default method for closing the frame
        f.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e)
            {
                System.exit(0);
            }
        });

        // Adding the created objects
        // to the frame
        f.add(l1);
        f.add(t1);
        f.add(l2);
        f.add(t2);
        f.add(l3);
        f.add(j1);
        f.add(l4);
        f.add(j2);
        f.add(l5);
        f.add(t3);
        f.add(b1);
        f.add(b2);
        f.setLayout(null);
        f.setSize(700, 600);
        f.setVisible(true);
    }
    // Driver code
    public static void main(String args[])
    {
        StudentInfo();
    }
}
