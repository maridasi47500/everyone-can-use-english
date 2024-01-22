VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} UserForm1 
   Caption         =   "UserForm1"
   ClientHeight    =   8325.001
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   9930.001
   OleObjectBlob   =   "UserForm1.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "UserForm1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub CommandButton1_Click()
LookUpMerriamWebsterDictionary
Exit Sub


End Sub
'?????,?????Merriam-Webster Collegiate Dictionary
Sub LookUpMerriamWebsterDictionary()
'MWDictionary Macro
Dim mot
mot = Selection.Text

Dim response
'response = MsgBox(Selection.Text)
Selection.MoveLeft Unit:=wdWord, Count:=1
Selection.MoveRight Unit:=wdWord, Count:=1, Extend:=wdExtend
Selection.Copy
Selection.MoveRight Unit:=wdWord, Count:=1
If Tasks.Exists("Merriam-Webster") = True Then
    'response = MsgBox("Task Merriam-Webster ok")
    With Tasks("Merriam-Webster")
        .Activate
        .WindowState = wdWindowStateNormal
    End With
    
    SendKeys mot & "{ENTER}", 1
Else
    response = MsgBox("Task Merriam-Webster doesn't exist! Run the application before use this Macro, please.", vbExclamation, "WARNING!")
End If
End Sub

Sub SpeakTheWord()
    On Error Resume Next
    Set speech = NewSpVoice
    
    Selection.MoveLeft Unit:=wdWord, Count:=1
    Selection.MoveRight Unit:=wdWord, Count:=1, Extend:=wdExtend
    If Len(Selection.Text) > 1 Then 'speak selection
        speech.Speak Trim(Selection.Text), _
        SVSFlagsAsync + SVSFPurgeBeforeSpeak
    End If
    Selection.MoveRight Unit:=wdWord, Count:=1
    Do
        DoEvents
    Loop Until speech.WaitUntilDone(10)
    Set speech = Nothing
End Sub

' ???????????
Sub AddDoubleQuotationMarks()
    Selection.InsertBefore ("“")
    Selection.InsertAfter ("”")
    Selection.MoveRight Unit:=wdWord, Count:=1
End Sub

' ?????????
Sub ChangeFontNameTo()
    Selection.Font.Name = "Georgia"
End Sub

' ???????????
Sub ChangeFontSizeTo()
    Selection.Font.Size = 28
End Sub

' ??????????
Sub FontSizeGrow()
    Selection.Font.Grow
End Sub

' ??????????
Sub FontSizeShrink()
    Selection.Font.Shrink
End Sub

' ???????????????
Sub FirstLetterToUppercase()
    Selection.MoveLeft Unit:=wdWord, Count:=1
    Selection.MoveRight Unit:=wdCharacter, Count:=1, Extend:=wdExtend
    Selection.Text = UCase(Selection.Text)
    Selection.MoveRight Unit:=wdWord, Count:=1
End Sub





Private Sub CommandButton2_Click()
Me.SpeakTheWord
Exit Sub

End Sub

Private Sub CommandButton3_Click()
Me.FontSizeShrink
Exit Sub
End Sub

Private Sub CommandButton4_Click()
Me.FirstLetterToUppercase
Exit Sub
End Sub

Private Sub CommandButton5_Click()
Me.FontSizeGrow
Exit Sub
End Sub

Private Sub CommandButton6_Click()
Me.ChangeFontNameTo
Exit Sub
End Sub

Private Sub CommandButton7_Click()
Me.ChangeFontSizeTo
Exit Sub
End Sub

Private Sub CommandButton8_Click()
Exit Sub

End Sub

Private Sub UserForm_Click()

End Sub

Private Sub UserForm_Initialize()

End Sub
