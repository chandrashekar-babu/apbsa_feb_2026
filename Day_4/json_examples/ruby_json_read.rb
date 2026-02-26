require 'json'
JSON.load(File.open("a.json")).each { |k, v|
            puts "#{k} -> #{v}\n" 
}


