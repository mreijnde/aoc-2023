% AOC2023 - day01

filename = "day01_input.txt";

% read datafile
lines = readlines(filename);

% part 1
total = 0;
for i=1:length(lines)    
    digits = extract(lines(i), digitsPattern(1));
    number = str2num( digits(1)+digits(end));
    total = total + number;
end
total

% part 2
keys   = ["1","2","3","4","5","6","7","8","9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
values = [1:9, 1:9];

total = 0;
for i=1:length(lines)
    line = char(lines(i));
    digit_start = findFirstDigit(line, keys, values);    
    digit_end   = findLastDigit(line, keys, values);
    number = 10*digit_start + digit_end;
    total = total + number;
end
total


function digit=findFirstDigit(line, keys, values)
digit=NaN;
for j=1:length(line)
    for k=1:length(values)
        if startsWith(line(j:end), keys(k))
            digit = values(k);
            return 
        end          
    end
end   
end


function digit=findLastDigit(line, keys, values)
digit=NaN;
for j=1:length(line)
    for k=1:length(values)
        if endsWith(line(1:end-j+1), keys(k))
            digit = values(k);
            return 
        end          
    end
end   
end
