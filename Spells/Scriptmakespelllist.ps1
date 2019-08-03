$csv = Import-Csv "D:\Python Projects\LifePath_CharGenerator\Spells\FullList.csv"

$spells = @{"Cantrip" = @(); "Level01" = @(); "Level02" = @(); "Level03" = @(); "Level04" = @(); "Level05" = @(); "Level06" = @(); "Level07" = @(); "Level08" = @(); "Level09" = @(); "Level10" = @()}

foreach ($i in $csv){
    #Write-Host $i.Name
    #$i.Level
    switch ($i.Level.Trim('')){
    "Cantrip" {$spells.Cantrip += $i.name; break}
    "10th" {$spells.Level10 += $i.name; break}
    "2nd" {$spells.Level02 += $i.name; break}
    "3rd" {$spells.Level03 += $i.name; break}
    "4th" {$spells.Level04 += $i.name; break}
    "5th" {$spells.Level05 += $i.name; break}
    "6th" {$spells.Level06 += $i.name; break}
    "7th" {$spells.Level07 += $i.name; break}
    "8th" {$spells.Level08 += $i.name; break}
    "9th" {$spells.Level09 += $i.name; break}
    "1st" {$spells.Level01 += $i.name; break}
    default {write-host $i.Name Failed}
    }
}
<#
foreach ($i in $spells.Level01){
    Write-Host "'$i',"
}
#>